from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())


class RecipeForm(forms.ModelForm):
    """ CREATE RECIPE FORM """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'ingredients',
            'instructions',
            'image',
            'image_alt',
            'meal_type',
            'cuisine_types',
            'calories'
            ]
        
        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())
        
        widget = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
        
        labels = {
            'title': 'Recipe Title',
            'description': 'Description',
            'ingredients': 'Recipe Ingredients',
            'instructions': 'Recipe instructions',
            'image': 'Recipe Image',
            'image_alt': 'Describe Image',
            "meal_type": "Meal Type",
            "cuisine_types": "Cuisine Type",
            "calories": "Calories",
            
        }