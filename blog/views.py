from django.views.generic import ListView
from .models import Stories

class DarkHomePageView(ListView):
    model = Stories
    template_name = 'dark-home.html'

class HomePageView(ListView):
    model = Stories
    template_name = 'home.html'