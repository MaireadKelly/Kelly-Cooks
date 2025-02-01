from django import forms
from djrichtextfield.widgets import RichTextWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Button
from .models import Recipe, Review


class RecipeForm(forms.ModelForm):
    """
    Form to create or edit a recipe.
    """

    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 8,
                    "placeholder": "Enter a brief description of the recipe",
                }
            ),
            "ingredients": RichTextWidget(
                attrs={"placeholder": "List the ingredients with quantities"}
            ),
            "instructions": RichTextWidget(
                attrs={"placeholder": "Provide step-by-step instructions"}
            ),
        }

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
    Form to add a review (comment) for a recipe.
    """

    class Meta:
        model = Review
        fields = ["comment"]

        widgets = {
            "comment": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Write your review here"}
            ),
        }
        labels = {
            "comment": "Your Review",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("comment", css_class="form-control mb-3"),
            Submit("submit", "Submit Review", css_class="btn btn-primary"),
            Button(
                "cancel",
                "Back to Recipe",
                css_class="btn btn-secondary",
                onclick="window.history.back()",
            ),
        )