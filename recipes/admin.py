from django.contrib import admin

from .models import Recipe, Review

# Admin configuration for the Recipe model


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "description",
        "ingredients",
        "instructions",
        "get_reviews_count",  # Updated field for displaying review count
        "created_at",
        "updated_at",
        "image",
    )

    # list_filter = ("title",)

    def get_reviews_count(self, obj):
        """
        Display the count of reviews related to the recipe.
        Assumes a related_name 'reviews' on the ForeignKey in the Review model.
        """
        return obj.reviews.count()

    get_reviews_count.short_description = (
        "Review Count"  # Column header in the admin list view
    )


# Admin configuration for the Review model


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "user",
        "comment",  # Assumes there's a 'comment' field in the Review model
        "created_at",
    )
    list_filter = ("user", "comment")  # Sidebar filters
    search_fields = (
        "comment",
        "user__username",
        "recipe__title",
    )  # Search functionality

