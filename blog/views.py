from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
# Local imports
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
