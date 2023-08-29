from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Story,StoryAttachement
from .serializers import StorySerializer

# Create your views here.

class CreateStory(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        user = request.user
        data = request.data
        attachement = data.get('url')
        isStory = None
        try:
            isStory = Story.objects.get(user=user)
        except:
            pass
        if isStory:
            attach = StoryAttachement.objects.create(story=isStory, url=attachement)
            attach.save()
            serializer = StorySerializer(isStory)
            return Response(serializer.data)
        else:
            story = Story.objects.create(user=user)
            story.save()
            attache = StoryAttachement.objects.create(story=story, url=attachement)
            attache.save()
            serializer = StorySerializer(story)
            return Response(serializer.data)
        

class GetStory(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        user = request.user
        followers = user.following.all().values_list('followers',flat=True)
        followers_list = list(followers)
        followers_stories = Story.objects.filter(user_id__in = followers_list).order_by('-time_stamp')
        user_stories = Story.objects.filter(user=user)
        combined_stories = followers_stories | user_stories
        serializer = StorySerializer(combined_stories, many=True)
        return Response(serializer.data)
    

class DeleteStory(APIView):
    def delete(self,request, storyId):
        story = Story.objects.get(id=storyId)
        story.delete()
        return Response({'response':'story deleted'})

