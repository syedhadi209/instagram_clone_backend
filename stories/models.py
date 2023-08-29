from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    time_stamp = models.DateTimeField(auto_now_add=True)


class StoryAttachement(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='urls')
    url = models.CharField(max_length=100)
