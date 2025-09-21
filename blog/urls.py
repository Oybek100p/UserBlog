from django.urls import path
from . import views

urlpatterns = [
    # Creators
    path('creators/', views.creator_list, name='creators'),
    path('creators/add/', views.creator_create, name='creator_create'),
    path('creators/<int:pk>/', views.creator_detail, name='creator_detail'),
    path('creators/<int:pk>/edit/', views.creator_update, name='creator_update'),
    path('creators/<int:pk>/delete/', views.creator_delete, name='creator_delete'),

    # Posts
    path('posts/', views.post_list, name='posts'),
    path('posts/add/', views.post_create, name='post_create'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
