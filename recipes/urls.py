from django.urls import path
from .views import (
    AddRecipe, Recipes, RecipeDetail, DeleteRecipe, EditRecipe, FavouritesView,
    toggle_like_recipe, favorite_recipe, add_review, rate_recipe
)

urlpatterns = [
    path('', Recipes.as_view(), name='recipes'),
    path('add/', AddRecipe.as_view(), name='add_recipe'),
    path('<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('edit/<int:pk>/', EditRecipe.as_view(), name='edit_recipe'),
    path('delete/<int:pk>/', DeleteRecipe.as_view(), name='delete_recipe'),
    path('<int:recipe_id>/like/', toggle_like_recipe, name='toggle_like_recipe'),
    path('<int:recipe_id>/favorite/', favorite_recipe, name='favorite_recipe'),
    path('<int:recipe_id>/review/', add_review, name='add_review'),
    path('favourites/', FavouritesView.as_view(), name='favourites'),
    path('<int:recipe_id>/rate/', rate_recipe, name='rate_recipe'),
]
