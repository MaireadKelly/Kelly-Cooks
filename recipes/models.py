from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


class Recipe(models.Model):
    """
    A model to create and manage basic recipes
    """
    user = models.ForeignKey(User, related_name='recipe_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(null=False, blank=False)  # Simplified this field
    ingredients = models.TextField(null=False, blank=False)  # TextField for rich text support
    instructions = RichTextField(max_length=10000, null=False, blank=False)  # TextField for rich text support
    created_at = models.DateTimeField(auto_now_add=False)  # Automatically set the timestamp on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update timestamp on modification
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='recipes/', force_format='WEBP',
        blank=False, null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)

    #class Meta:
    #    ordering = ['-created_at']

    def __str__(self):
        return self.title
