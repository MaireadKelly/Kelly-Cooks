from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import AddRecipe, Recipes, RecipeDetail, DeleteRecipe, EditRecipe, test_image_upload, favorite_recipe, add_review


urlpatterns = [
    path('test-upload/', test_image_upload, name='test_image_upload'),
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("djrichtextfield/", include("djrichtextfield.urls")),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe"),
#    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('favorite/<int:recipe_id>/', favorite_recipe, name='favorite_recipe'),
    path('recipe/<int:recipe_id>/review/', add_review, name='add_review'),
    # Add more URLs for features like Review, Follow, and Favorite here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


