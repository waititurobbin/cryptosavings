from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'savings/home.html')

def about_view(request):
    return render(request, 'savings/about.html')

def contacts_view(request):
    return render(request, 'savings/contacts.html')
