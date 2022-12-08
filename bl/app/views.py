from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import *
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    context_object_name = 'all_Post_list'
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'all_Post_detail'
    template_name = 'blog.html'

class BlogNewView(CreateView):
    template_name = 'new_blog.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogEditView(UpdateView):
    model = Post
    template_name = 'edit_blog.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('BlogListView') 
