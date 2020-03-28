from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Blog App Homepage</h1>")

def about(request):
    return HttpResponse("<h1>Blog App About page</h1>")
