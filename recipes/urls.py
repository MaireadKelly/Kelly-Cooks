from django.urls import path

from .views import (
    Recipes,
    RecipeDetail,
    AddRecipe,
    EditRecipe,
    DeleteRecipe,
    MyRecipes,
    MyFavourites,
    add_review,
    delete_review,
    edit_review,
    toggle_favourite,  # function view we’re using
)

app_name = "recipes"

urlpatterns = [
    path("", Recipes.as_view(), name="recipes"),
    path("<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("edit/<int:pk>/", EditRecipe.as_view(), name="edit_recipe"),
    path("delete/<int:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("my-recipes/", MyRecipes.as_view(), name="my_recipes"),
    path("favourites/", MyFavourites.as_view(), name="favourites"),
    path("<int:pk>/favourite/", toggle_favourite, name="favourite_toggle"),
    path(
        "<int:pk>/review/", add_review, name="add_review"
    ),
    path(
        "review/<int:pk>/edit/", edit_review, name="edit_review"
    ),
    path("review/<int:pk>/delete/", delete_review, name="delete_review"),
]
