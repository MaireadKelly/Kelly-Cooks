from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipeForm  # Ensure your RecipeForm matches the simplified model

from django.http import HttpResponse
from cloudinary.uploader import upload

def test_image_upload(request):
    # Path to a local image or one you have in your project folder
    image_path = 'path_to_image_on_your_system.jpg'
    
    # Upload the image to Cloudinary
    result = upload(image_path)
    
    # Get the Cloudinary URL for the uploaded image
    uploaded_image_url = result.get('url')
    
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
    paginate_by = 10


class RecipeDetail(DetailView):
    """VIEW A SINGLE RECIPE"""

    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"
