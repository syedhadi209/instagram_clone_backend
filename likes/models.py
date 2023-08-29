from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from posts.models import Post

# Create your models here.

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
