# Generated by Django 5.1.1 on 2024-09-19 17:38

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0006_alter_recipe_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=cloudinary.models.CloudinaryField(
                max_length=255, verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
