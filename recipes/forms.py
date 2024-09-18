from django.db import models
from datetime import timedelta
from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe

class TimestampsWithAuto(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class RecipeForm(forms.ModelForm):
    """ FORM TO CREATE A RECIPE """
    
    class Meta:
        model = Recipe
        fields = ["title", "description", "ingredients", "instructions", "image", "image_alt"]
        
        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())
        created_on = models.DateTimeField(auto_now=True)

        
        widget = {
           "description": forms.Textarea(attrs={"rows": 5}),
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
