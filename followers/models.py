from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Follow(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following',null=True, blank=True)
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers',null=True, blank=True)
    accepted = models.BooleanField(default=False)
