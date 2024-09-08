from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


# CHOICE FIELDS
MY_RECIPES = (
    ('my_recipes', 'My Recipes'),
    ('saved_recipes', 'My Saved Recipes'),
    ('create_recipe', 'Create New Recipe',)
)

class Recipe(models.Model):
    """
    A model to create and manage recipes
    """
    user = models.ForeignKey(User, related_name='recipe_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None], 
        quality=75, 
        upload_to='recipes/', 
        force_format='WEBP',
        blank=False, 
        null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    my_recipes = models.CharField(max_length=50, choices=MY_RECIPES)
    saved_recipes = models.CharField(max_length=50, null=False, blank=False)
    create_recipe = RichTextField(max_length=10000, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.title)





