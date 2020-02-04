from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, #from blog views.py
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #url extention
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'), #url extention
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), 
    path('about/',views.about, name='blog-about'),
]