from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class index(TemplateView):
    template_name = 'home/index.html'
