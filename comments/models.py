from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
