from django.urls import path
from .views import *

urlpatterns = [
    path('add-story/', CreateStory.as_view()),
    path('get-stories/', GetStory.as_view()),
    path('delete-story/<storyId>/',DeleteStory.as_view())
]