from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import *

class BlogListView(ListView):
    model = Post
    context_object_name = 'all_Post_list'
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'all_Post_detail'
    template_name = 'blog.html'

class BlogNewView(CreateView):
    model = Post
    template_name = 'new_blog.html'
    fields = ['title', 'author', 'body']
    
