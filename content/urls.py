
//Project level

from django.urls import path
from .import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name = 'post_list'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/view/<int:pk>/', views.PostView.as_view(), name='post_view'),
    path('posts/edit/<int:pk>/', views.PostEditView.as_view(), name='post_edit'),
    path('posts/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),


]
