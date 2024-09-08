from django.contrib import admin
from .models import Recipe

# Register your models here.
@admin.register(Recipe)
class  RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'my_recipes',
        'ingredients',
        'instructions',
        'image'
    )
    
    list_filter = ('my_recipes',)