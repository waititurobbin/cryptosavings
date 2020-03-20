from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_view, name='savings-home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('about/', views.about_view, name='savings-about'),
    path('contacts/', views.contacts_view, name='savings-contacts'),
]
