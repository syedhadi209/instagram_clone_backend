from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField(null=True)
    time_created = models.DateTimeField(auto_now_add=True)



class Attachements(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="attachements")
    url = models.CharField(max_length=500)
