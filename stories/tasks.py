from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Story

@shared_task
def delete_expired_stories():
    expired_stories = Story.objects.filter(time_stamp__lt=timezone.now() - timedelta(hours=1))
    expired_stories.delete()