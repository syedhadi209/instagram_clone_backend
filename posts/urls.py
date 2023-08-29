from django.urls import path
from .views import *


urlpatterns = [
    path('create-post/', CreatePost.as_view()),
    path('get-posts/', GetPosts.as_view()),
    path('delete-post/<postId>/', DeletePost.as_view()),
    path('update-post/<postId>/', UpdatePost.as_view()),
    path('profile-posts/', GetProfilePosts.as_view())
]