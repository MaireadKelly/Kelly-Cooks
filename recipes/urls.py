from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AddRecipe, Recipes, RecipeDetail  # Import the views correctly

from django.urls import path
from .views import test_image_upload

urlpatterns = [
    path('test-upload/', test_image_upload, name='test_image_upload'),
]


urlpatterns = [
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("recipes/", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    # path("djrichtextfield/", include("djrichtextfield.urls")),
    # path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    # path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe",)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)