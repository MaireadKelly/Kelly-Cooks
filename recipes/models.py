from cloudinary.models import CloudinaryField
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


class Recipe(models.Model):
    """
    A model to create and manage basic recipes
    """

    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)  # Simplified this field
    ingredients = models.TextField(
        null=False, blank=False
    )  # TextField for rich text support
    instructions = RichTextField(
        max_length=10000, null=False, blank=False
    )  # TextField for rich text support
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Automatically set the timestamp on creation
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Automatically update timestamp on modification
    image = CloudinaryField("image", blank=False, null=False)

    # image = ResizedImageField(
    #    size=[400, None],
    #    quality=75,
    #    upload_to="recipes/",
    #    force_format="WEBP",
    #    blank=False,
    #    null=False,
    # )
    image_alt = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
    
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'followed')
        
    def __str__(self):
        return f"{self.follower} follows {self.follwed}"
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ("user", "recipe")
        
        def __str__(self):
            return f"{self.user} favorited {self.recipe}"
        
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __set__(self):
        return f"Review by {self.user} on {self.recipe}"
    
