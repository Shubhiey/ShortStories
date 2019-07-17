from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name= 'home'),
    path('dark-home/', views.DarkHomePageView.as_view(), name= 'dark-home'),
]
