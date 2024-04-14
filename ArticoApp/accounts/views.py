from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# classes with call


def register(request):
    context = {}
    return render(request, 'register.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def show_author_profile(request, auth_slug):
    context = {}

    return render(request, 'author-profile.html', context)