from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe, Review
from django_resized import ResizedImageField


class RecipeForm(forms.ModelForm):
    """
    Form to create or edit a recipe.
    This form includes fields for the recipe title, description, ingredients,
    instructions, image, and image_alt.
    """
    class Meta:
        model = Recipe
        fields = ["title", "description", "ingredients", "instructions", "image", "image_alt"]

        # Custom widgets and field settings for better user input
        widgets = {
            "description": forms.Textarea(attrs={"rows": 8, "placeholder": "Enter a brief description of the recipe"}),
            "ingredients": RichTextWidget(attrs={"placeholder": "List the ingredients with quantities"}),
            "instructions": RichTextWidget(attrs={"placeholder": "Provide step-by-step instructions"}),
        }

        # Custom labels for the form fields
        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "image": "Recipe Image",
            "image_alt": "Image Alt Text",
        }


class ReviewForm(forms.ModelForm):
    """
    Form to add a review for a recipe.
    This form allows users to provide a rating (1-5 stars) and a comment.
    """
    class Meta:
        model = Review
        fields = ["rating", "comment"]

        # Custom widgets for better review submission experience
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5, "placeholder": "Rate 1-5"}),
            "comment": forms.Textarea(attrs={"rows": 4, "placeholder": "Write your review here"}),
        }

        # Custom labels for review form fields
        labels = {
            "rating": "Rating (1-5)",
            "comment": "Review Comment",
        }
