from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from .models import Recipe, Favorite, Review
from .forms import RecipeForm, ReviewForm
from random import sample


class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Recipes(ListView):
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"
    paginate_by = 10

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            return self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(instructions__icontains=query)
            )
        return self.model.objects.all()


class RecipeDetail(DetailView):
    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm

    def get_success_url(self):
        return self.object.get_absolute_url()

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "recipes/confirm_delete.html"
    model = Recipe
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        messages.success(request, "The recipe has been deleted successfully!")
        return super().delete(request, *args, **kwargs)


class FavouritesView(ListView):
    model = Favorite
    template_name = 'recipes/favourites.html'
    context_object_name = 'favourites'

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


@login_required
def toggle_like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        messages.info(request, "You unliked this recipe.")
    else:
        recipe.likes.add(request.user)
        messages.success(request, "You liked this recipe.")
    return redirect("recipe_detail", pk=recipe_id)


@login_required
def favorite_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    return redirect("recipe_detail", pk=recipe_id)


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
        form = ReviewForm()
    return render(request, "recipes/add_review.html", {"form": form, "recipe": recipe})
