from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='savings-home'),
    path('about/', views.home, name='savings-about'),
]
