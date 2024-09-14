from django.urls import path
from .views import AddRecipe, Recipes  # Import the views correctly

urlpatterns = [
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("recipes/", Recipes.as_view(), name="recipes"),
]
