from django.urls import path
from .views import *


urlpatterns = [
    path('like-post/<postId>/<userId>/', LikePost.as_view()),
    path('get-likes/<postId>/', GetLikes.as_view())
]