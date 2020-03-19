from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='savings-home'),
    path('about/', views.about_view, name='savings-about'),
    path('contacts/', views.contacts_view, name='savings-contacts'),
]
