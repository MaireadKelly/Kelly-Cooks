from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import AddRecipe, Recipes, RecipeDetail, DeleteRecipe, EditRecipe, FavouritesView, favorite_recipe, add_review

urlpatterns = [

    path('add/', AddRecipe.as_view(), name='add_recipe'),
    path('', Recipes.as_view(), name='recipes'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('delete/<int:pk>/', DeleteRecipe.as_view(), name='delete_recipe'),
    path('edit/<int:pk>/', EditRecipe.as_view(), name='edit_recipe'),
    path('favorite/<int:recipe_id>/', favorite_recipe, name='favorite_recipe'),
    path('recipe/<int:recipe_id>/review/', add_review, name='add_review'),
    path('favourites/', FavouritesView.as_view(), name='favourites'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
