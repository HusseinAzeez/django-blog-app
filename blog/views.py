from django.shortcuts import render
from django.http import HttpResponse
# Local imports
from blog.models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Homepage'
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'about.html', context)
