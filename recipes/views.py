from datetime import timedelta
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin)
from .models import Recipe
from .forms import RecipeForm
from django.http import HttpResponse
from cloudinary.uploader import upload
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Follow



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
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(ingredients__icontains=query)
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
    """ EDIT A RECIPE """
    template_name = 'recipes/edit_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'
    
    def test_func(self):
        return self.request.user == self.get_object().user
    
class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ DELETE A RECIPE """
    template_name = 'recipes/'
    model = Recipe
    success_url = '/recipes/'
    
    def test_func(self):
        return self.request.user == self.get_object().user
    
@login_required
def follow_user(request, user_id):
    followed_user = User.objects.get(id=user_id)
    follow, created = Follow.objects.get_or_create(follower=request.user, followed=followed_user)
    
    if created:
        return redirect('profile', user_id=user_id)
    else:
        return redirect('profile', user_id=user_id)
        
