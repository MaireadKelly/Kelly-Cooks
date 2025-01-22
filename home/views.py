from django.views.generic import TemplateView
from recipes.models import Recipe
from random import sample
from django.db.models import Count


class IndexView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_recipes = Recipe.objects.all()
        context["random_recipes"] = sample(list(all_recipes), min(len(all_recipes), 4))
        return context
