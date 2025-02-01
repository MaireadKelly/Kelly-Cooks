from django.urls import path
from .views import (
    AddRecipe,
    Recipes,
    RecipeDetail,
    DeleteRecipe,
    EditRecipe,
    add_review,
    edit_review,
    delete_review,
    MyRecipes,
    MyFavourites,
    toggle_favourite,
)

urlpatterns = [
    path("", Recipes.as_view(), name="recipes"),
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("edit/<int:pk>/", EditRecipe.as_view(), name="edit_recipe"),
    path("delete/<int:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("<int:recipe_id>/review/", add_review, name="add_review"),
    path("review/<int:review_id>/edit/", edit_review, name="edit_review"),
    path(
        "review/<int:review_id>/delete/",
        delete_review,
        name="delete_review",
    ),
    path("my-recipes/", MyRecipes.as_view(), name="my_recipes"),
    path("favourites/", MyFavourites.as_view(), name="favourites"),
    path(
        "recipe/<int:recipe_id>/toggle-favourite/",
        toggle_favourite,
        name="toggle_favourite",
    ),
]