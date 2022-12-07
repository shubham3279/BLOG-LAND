from django.views.generic import ListView, DetailView
from .models import *

class BlogListView(ListView):
    model = Post
    context_object_name = 'all_Post_list'
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'all_Post_detail'
    template_name = 'blog.html'


