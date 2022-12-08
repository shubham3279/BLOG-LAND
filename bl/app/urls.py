from django.urls import path 
from .views import *

urlpatterns = [
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='BlogDeleteView'),
    path('blog/<int:pk>/edit/', BlogEditView.as_view(), name='BlogEditView'),
	path('',BlogListView.as_view(), name='BlogListView'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='BlogDetailView'),
    path('blog/new/', BlogNewView.as_view(), name = 'BlogNewView')
	]