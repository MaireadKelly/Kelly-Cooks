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
    # list & detail
    path("", Recipes.as_view(), name="recipes"),
    path("<int:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    # CRUD
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("edit/<int:pk>/", EditRecipe.as_view(), name="edit_recipe"),
    path("delete/<int:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    # user lists
    path("my-recipes/", MyRecipes.as_view(), name="my_recipes"),
    path("favourites/", MyFavourites.as_view(), name="favourites"),
    # favourites (recipe pk) — toggle add/remove via POST
    path("<int:pk>/favourite/", toggle_favourite, name="favourite_toggle"),
    # reviews
    path(
        "<int:pk>/review/", add_review, name="add_review"
    ),  # add review to recipe (recipe pk)
    path(
        "review/<int:pk>/edit/", edit_review, name="edit_review"
    ),  # edit a review (review pk)
    path("review/<int:pk>/delete/", delete_review, name="delete_review"),
]
