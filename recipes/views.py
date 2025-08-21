from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages import get_messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import RecipeForm, ReviewForm
from .models import Favourite, Recipe, Review


"""
View for users to add a new recipe
"""


class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm

    def form_valid(self, form):  # Associate logged in user with the new recipe
        form.instance.user = self.request.user
        messages.success(self.request, "Your recipe has been added successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


"""
View to list all recipes with optional search functionality
"""


class Recipes(ListView):
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 12

    def get_queryset(self, **kwargs):  # Filter recipes based on search query
        query = self.request.GET.get("q")
        if query:
            return self.model.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(ingredients__icontains=query)
                | Q(instructions__icontains=query)
            )
        return self.model.objects.all()


"""
View to display a single recipe's details
"""


class RecipeDetail(DetailView):
    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context["reviews"] = recipe.reviews.all()[:5]  # Show latest 5 reviews
        if self.request.user.is_authenticated:
            context["is_favourite"] = recipe.favourite_set.filter(
                user=self.request.user
            ).exists()
        else:
            context["is_favourite"] = False
        return context


"""
View to see logged in users' own recipes
"""


class MyRecipes(LoginRequiredMixin, ListView):
    template_name = "recipes/my_recipes.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)


"""
View to see logged in users' favourites
"""


class MyFavourites(LoginRequiredMixin, ListView):
    template_name = "recipes/favourites.html"
    model = Favourite
    context_object_name = "favourites"

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user)


"""
View for users to edit their own recipes
"""


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm

    def form_valid(self, form):
        messages.success(self.request, "Your recipe has been updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user == self.get_object().user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            obj = self.get_object()
            messages.error(
                self.request, "You don’t have permission to edit this recipe."
            )
            return redirect("recipe_detail", pk=obj.pk)
        return super().handle_no_permission()


"""
View for users to delete their own recipes
"""


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipes")  # make sure this URL name exists

    # Only the owner may delete
    def test_func(self):
        obj = self.get_object()
        return obj.user_id == self.request.user.id

    # If user fails the ownership check, be graceful (no 403 / debug page)
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            try:
                obj = self.get_object()
                messages.error(
                    self.request, "You don’t have permission to delete this recipe."
                )
                return redirect("recipe_detail", pk=obj.pk)
            except Exception:
                # If object lookup itself fails, fall back safely
                messages.error(self.request, "You don’t have permission to do that.")
                return redirect("recipes")
        return super().handle_no_permission()

    # Perform delete with safe messaging
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        title = obj.title  # capture before delete
        try:
            response = super().delete(request, *args, **kwargs)
            messages.success(request, f"‘{title}’ was deleted successfully.")
            return response  # redirects to success_url
        except Exception:
            # Don’t expose internal errors in production
            messages.error(request, "Sorry, we couldn’t delete that recipe right now.")
            return redirect("recipes")


"""
Functions for reviews & favourites (normalized to pk)
"""


@login_required
def add_review(request, pk):
    """
    Add a review to a recipe (recipe pk).
    Only logged-in users can submit reviews.
    """
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
            return redirect("recipe_detail", pk=recipe.pk)
        else:
            messages.error(
                request, "There was an error in your form. Please try again."
            )
    else:
        form = ReviewForm()
    return render(request, "recipes/add_review.html", {"form": form, "recipe": recipe})


@login_required
def edit_review(request, pk):
    """
    Edit a review (review pk).
    """
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review has been updated successfully!")
            return redirect("recipe_detail", pk=review.recipe.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, "recipes/edit_review.html", {"form": form, "review": review})


@login_required
def delete_review(request, pk):
    """
    Delete a review (review pk).
    """
    review = get_object_or_404(Review, pk=pk)
    # Ensure only the review author can delete
    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect("recipe_detail", pk=review.recipe.pk)

    review.delete()
    messages.success(request, "Review successfully deleted!")
    return redirect("recipe_detail", pk=review.recipe.pk)


@login_required
def toggle_favourite(request, pk):
    """
    Toggle favourite for the given recipe (recipe pk).
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    favourite, created = Favourite.objects.get_or_create(
        user=request.user, recipe=recipe
    )
    if not created:
        favourite.delete()
        messages.success(request, "Recipe removed from favourites.")
    else:
        messages.success(request, "Recipe added to favourites.")
    return redirect("recipe_detail", pk=recipe.pk)


def custom_404_view(request, exception):
    return render(request, "404.html", status=404)
