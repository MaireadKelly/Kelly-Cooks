from django.contrib import admin
from .models import Recipe, Review


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "description",
        "ingredients",
        "instructions",
        "created_at",
        "updated_at",
        "image",
    )

    # list_filter = ("title",)
