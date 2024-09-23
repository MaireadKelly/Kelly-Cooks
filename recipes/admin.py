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

    from django.contrib import admin


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe", "rating", "created_at")  # Adjust fields as needed
    search_fields = (
        "user__username",
        "recipe__title",
        "rating",
    )  # Make fields searchable


admin.site.register(Review, ReviewAdmin)


# list_filter = ("title",)
