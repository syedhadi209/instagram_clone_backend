from django.urls import path
from .views import *

urlpatterns = [
    path('add-comment/<postId>/',AddComment.as_view()),
    path('delete-comment/<commentId>/', DeleteComment.as_view()),
    path('update-comment/<commentId>/', UpdateComment.as_view())
]