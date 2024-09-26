from django.db import models
from datetime import timedelta
from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe, Review
from django_resized import ResizedImageField


class TimestampsWithAuto(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RecipeForm(forms.ModelForm):
    """FORM TO CREATE A RECIPE"""

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

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())
        created_on = models.DateTimeField(auto_now=True)
        image = ResizedImageField(
            size=[400, None],
            quality=75,
            upload_to="recipes/",
            force_format="WEBP",
            blank=False,
            null=False,
        )

        widget = {
            "description": forms.Textarea(attrs={"rows": 8}),
        }

        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "image_alt": "Describe Image",
            "created_on": "Date posted",
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]
