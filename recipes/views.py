from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from .models import Recipe, Review
from .forms import RecipeForm, ReviewForm
from django.http import JsonResponse

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
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(instructions__icontains=query)
            )
        return self.model.objects.all()

""" 
View to display a single recipe's details
"""
class RecipeDetail(DetailView):
    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"
    
    def get_context_data(self, **kwargs): # Add context data for likes and average rating
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()
        context['reviews'] = recipe.review_set.all()
        return context

"""
View for users to edit their own recipes
"""
class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm

    def get_success_url(self): # redirect to the updated recipe's detail view
        return self.object.get_absolute_url()

    def test_func(self): # Ensure that only the recipe owner can edit the recipe
        return self.request.user == self.get_object().user

"""
View for users to delete their own recipes
"""
class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "recipes/confirm_delete.html"
    model = Recipe
    success_url = "/recipes/"

    def test_func(self): # Ensure that only the recipe owner can delete the recipe
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        messages.success(request, "The recipe has been deleted successfully!")
        return super().delete(request, *args, **kwargs)


"""
Function to add a review to a recipe
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
        form = ReviewForm()
    return render(request, "recipes/add_review.html", {"form": form, "recipe": recipe})
