from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
from .models import Recipe, Review, Favourite
from .forms import RecipeForm, ReviewForm

"""
View for users to add a new recipe
"""


class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):  # Associate the logged in user with the new recipe
        form.instance.user = self.request.user
        return super().form_valid(form)


""" 
View to list all recipes with optional search functionality
"""


class Recipes(ListView):
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 10

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
        context["reviews"] = recipe.reviews.all()
        if self.request.user.is_authenticated:
            context["is_favourite"] = recipe.favourite_set.filter(
                user=self.request.user
            ).exists()
        else:
            context["is_favourite"] = False
        return context


"""
View to see logged in Users Own recipes
"""


class MyRecipes(LoginRequiredMixin, ListView):
    template_name = "recipes/my_recipes.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)


"""
View to see logged in Users Favourites
"""


class MyFavourites(LoginRequiredMixin, ListView):
    template_name = "recipes/favourites.html"
    model = Favourite
    context_object_name = "favourites"

    def get_queryset(self):
        # Ensure this filters only valid favourites tied to the user
        return Favourite.objects.filter(user=self.request.user)


"""
View for users to edit their own recipes
"""


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm

    def get_success_url(self):  # Redirect to the updated recipe's detail view
        return self.object.get_absolute_url()

    def test_func(self):  # Ensure that only the recipe owner can edit the recipe
        return self.request.user == self.get_object().user


"""
View for users to delete their own recipes
"""


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "recipes/confirm_delete.html"
    model = Recipe
    success_url = "/recipes/"

    def test_func(self):  # Ensure that only the recipe owner can delete the recipe
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        messages.success(request, "The recipe has been deleted successfully!")
        return super().delete(request, *args, **kwargs)


"""
Function to add a review (comment) to a recipe
"""


@login_required
def add_review(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been added successfully!")
            return redirect("recipe_detail", pk=recipe.id)
        else:
            messages.error(
                request, "There was an error in your submission. Please try again."
            )
    else:
        form = ReviewForm()
    return render(request, "recipes/add_review.html", {"form": form, "recipe": recipe})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review has been updated successfully!")
            return redirect("recipe_detail", pk=review.recipe.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, "recipes/edit_review.html", {"form": form, "review": review})


@login_required
def delete_review(request, review_id):
    """
    View to delete a specific review.
    """
    review = get_object_or_404(Review, id=review_id)
    # Ensure the logged-in user is the author of the review
    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return HttpResponseRedirect(reverse("recipe_detail", args=[review.recipe.id]))

    review.delete()
    messages.success(request, "Review successfully deleted!")
    return HttpResponseRedirect(reverse("recipe_detail", args=[review.recipe.id]))


@login_required
def toggle_favourite(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favourite, created = Favourite.objects.get_or_create(
        user=request.user, recipe=recipe
    )
    if not created:
        favourite.delete()
        messages.success(request, "Recipe removed from favourites.")
    else:
        messages.success(request, "Recipe added to favourites.")
    return redirect("recipe_detail", pk=recipe.id)


def custom_404_view(request, exception):
    return render(request, "404.html", status=404)
