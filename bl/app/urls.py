from django.urls import path 
from .views import *

urlpatterns = [
    
	path('',BlogListView.as_view(), name='BlogListView'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='BlogDetailView'),
    
	]