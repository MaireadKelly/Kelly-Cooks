from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField

class Recipe(models.Model):
    """
    A model to create and manage recipes
    """
    user = models.ForeignKey(User, related_name='recipe_owner', on_delete=models.CASCADE)
    title = models.Charfiled(max_lenght=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = RichTextField(max_lenght=10000, null=False, blank=False)
    instructions = RichTextField(max_lenght=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='recipes/', force_format='WEBP',
        blank=False, null=False
    )




