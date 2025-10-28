from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages import get_messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import RecipeForm, ReviewForm
from .models import Favourite, Recipe, Review


"""
View for users to add a new recipe
"""


class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "Recipe added successfully!")
        return redirect("recipes:recipe_detail", pk=form.instance.pk)

    def get_success_url(self):
        return reverse("recipes:recipe_detail", kwargs={"pk": self.object.pk})


"""
View to list all recipes with optional search functionality
"""


class Recipes(ListView):
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 12

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        qs = self.model.objects.all()
        if query:
            qs = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(ingredients__icontains=query)
                | Q(instructions__icontains=query)
            )
        return qs.order_by("-id")


"""
View to display a single recipe's details
"""


class RecipeDetail(DetailView):
    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object
        try:
            context["reviews"] = recipe.reviews.order_by("-created_at")[:5]
        except Exception:
            context["reviews"] = recipe.reviews.all()[:5]
        if self.request.user.is_authenticated:
            context["is_favourite"] = Favourite.objects.filter(
                user=self.request.user, recipe=recipe
            ).exists()
        else:
            context["is_favourite"] = False
        return context


"""
View to see logged-in users' own recipes
"""


class MyRecipes(LoginRequiredMixin, ListView):
    template_name = "recipes/my_recipes.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user).order_by("-id")


"""
View to see logged-in users' favourites
"""


class MyFavourites(LoginRequiredMixin, ListView):
    template_name = "recipes/favourites.html"
    model = Favourite
    context_object_name = "favourites"

    def get_queryset(self):
        return (
            Favourite.objects.filter(user=self.request.user)
            .select_related("recipe", "user")
            .order_by("-id")
        )


"""
View for users to edit their own recipes (admins can edit any)
"""


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm

    def form_valid(self, form):
        messages.success(self.request, "Recipe updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        # owner OR superuser can edit

        return user.is_authenticated and (
            obj.user_id == user.id or user.is_superuser
        )

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            obj = self.get_object()
            messages.error(
                self.request, "You don’t have permission to edit this recipe."
            )
            return redirect("recipes:recipe_detail", pk=obj.pk)
        return super().handle_no_permission()


"""
View for users to delete their own recipes (admins can delete any)
"""


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipes:recipes")

    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        # owner OR superuser can delete

        return user.is_authenticated and (
            obj.user_id == user.id or user.is_superuser
        )

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            try:
                obj = self.get_object()
                messages.error(
                    self.request,
                    "You don’t have permission to delete this recipe.",
                )
                return redirect("recipes:recipe_detail", pk=obj.pk)
            except Exception:
                messages.error(
                    self.request, "You don’t have permission to do that."
                )
                return redirect("recipes:recipes")
        return super().handle_no_permission()

    # Queue message BEFORE calling super().delete (most reliable)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        title = self.object.title
        messages.success(request, f'"{title}" was deleted successfully.')
        return self.delete(request, *args, **kwargs)


"""
Functions for reviews & favourites (normalized to pk)
"""


@login_required
def add_review(request, pk):
    # Clear any previous messages

    storage = get_messages(request)
    for _ in storage:
        pass
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe
            review.user = request.user
            review.save()
            messages.success(request, "Review has been added successfully!")
            return redirect("recipes:recipe_detail", pk=recipe.pk)
        else:
            messages.error(
                request, "There was an error in your form. Please try again."
            )
    else:
        form = ReviewForm()
    return render(
        request, "recipes/add_review.html", {"form": form, "recipe": recipe}
    )


@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review has been updated successfully!")
            return redirect("recipes:recipe_detail", pk=review.recipe.pk)
    else:
        form = ReviewForm(instance=review)
    return render(
        request, "recipes/edit_review.html", {"form": form, "review": review}
    )


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if review.user != request.user and not request.user.is_superuser:
        messages.error(
            request, "You are not authorized to delete this review."
        )
        return redirect("recipes:recipe_detail", pk=review.recipe.pk)
    review.delete()
    messages.success(request, "Review successfully deleted!")
    return redirect("recipes:recipe_detail", pk=review.recipe.pk)


@login_required
@require_POST
def toggle_favourite(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    favourite, created = Favourite.objects.get_or_create(
        user=request.user, recipe=recipe
    )

    if created:
        messages.success(request, "Recipe added to favourites.")
    else:
        favourite.delete()
        messages.success(request, "Recipe removed from favourites.")
    # Optional safe redirect-back

    next_url = request.POST.get("next")
    if next_url and url_has_allowed_host_and_scheme(
        next_url, {request.get_host()}
    ):
        return redirect(next_url)
    return redirect("recipes:recipe_detail", pk=recipe.pk)


def custom_404_view(request, exception):
    return render(request, "404.html", status=404)
