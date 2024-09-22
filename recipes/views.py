from datetime import timedelta
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Recipe, Favorite, Review
from .forms import RecipeForm, ReviewForm
from django.http import HttpResponse
from cloudinary.uploader import upload
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def test_image_upload(request):
    # Path to a local image or one you have in your project folder

    image_path = "path_to_image_on_your_system.jpg"

    # Upload the image to Cloudinary

    result = upload(image_path)

    # Get the Cloudinary URL for the uploaded image

    uploaded_image_url = result.get("url")

    # Return the image URL in an HTTP response

    return HttpResponse(f"Uploaded image URL: {uploaded_image_url}")


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add recipe view"""

    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class Recipes(ListView):
    """LIST VIEW FOR ALL RECIPES"""

    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 3

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(instructions__icontains=query)
                | Q(ingredients__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes


class RecipeDetail(DetailView):
    """VIEW A SINGLE RECIPE"""

    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """EDIT A RECIPE"""

    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """DELETE A RECIPE"""

    template_name = "recipes/"
    model = Recipe
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user


@login_required
def favorite_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    favorite, created = Favorite.objects.get_or_create(
        user=request.user, recipe=recipe
    )

    if created:
        # SUCCESSFULLY FAVORITED

        return redirect("recipe_detail", pk=recipe_id)
    else:
        # ALREADY FAVORITED

        return redirect("recipe_detail", pk=recipe_id)


@login_required
def add_review(request, recipe_id):
    recipe = get_object_or_404(
        Recipe, id=recipe_id
    )  # Ensure the recipe exists

    if request.method == "POST":
        form = ReviewForm(request.POST)  # Initialize the form with POST data
        if form.is_valid():
            review = form.save(commit=False)  # Don't save yet
            review.recipe = recipe  # Associate with the recipe
            review.user = request.user  # Associate with the logged-in user
            review.save()  # Now save it
            messages.success(
                request, "Your review has been added successfully"
            )
            return redirect(
                "recipe_detail", pk=recipe.id
            )  # Redirect after success
    else:
        form = ReviewForm()  # Initialize the form for GET request

        return render(
            request,
            "recipes/add_review.html",
            {"form": form, "recipe": recipe},
        )
