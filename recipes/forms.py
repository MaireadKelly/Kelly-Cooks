from django import forms
from .models import Recipe
from djrichtextfield.widgets import RichTextWidget


class RecipeForm(forms.ModelForm):
    """ FORM TO CREATE A RECIPE """
    
    class Meta:
        model = Recipe
        fields = ["title", "description", "ingredients", "instructions", "image", "image_alt"]
        
        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())
        
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
        }
