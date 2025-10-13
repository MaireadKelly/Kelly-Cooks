from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.urls import reverse
from djrichtextfield.models import RichTextField


class Recipe(models.Model):
    """
    A model to create and manage basic recipes.
    """

    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    ingredients = models.TextField(null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField("image", blank=False, null=False)
    image_alt = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL for the detail view of a recipe instance.
        """
        return reverse("recipes:recipe_detail", kwargs={"pk": self.pk})


class Review(models.Model):
    """
    A model to store reviews (comments) for recipes.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} on {self.recipe}"


class Favourite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "recipe"], name="unique_user_recipe_favourite"
            )
        ]

    def __str__(self):
        return f"{self.user} → {self.recipe}"
