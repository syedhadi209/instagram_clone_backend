from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import PostSerializer,AttachementSerializer
from rest_framework.response import Response
from authentication.serializers import LoginUserSerializer
from .models import Post, Attachements
import time
from followers.models import Follow
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class CreatePost(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        user = request.user
        data = request.data
        description = data.get('caption')
        attachements = data.get('responses')
        post = Post.objects.create(user=user, description=description)
        post.save()
        for url in attachements:
            attach = Attachements.objects.create(url=url, post=post)
            attach.save()
        serializer = PostSerializer(post)
        return Response({'data': serializer.data})
    

class GetPosts(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        user = request.user
        user_following = Follow.objects.filter(user_id = user).values_list('followers',flat=True)
        user_following_ids = list(user_following)
        followers_posts = Post.objects.filter(user_id__in=user_following_ids).order_by('-time_created')
        user_post = Post.objects.filter(user = user)
        combined_posts = user_post | followers_posts
        serializer = PostSerializer(combined_posts, many=True)
        return Response(serializer.data)
    

class DeletePost(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self,request, postId):
        post = Post.objects.get(id=postId)
        post.delete()
        time.sleep(1)
        return Response({"response": postId})
    

class UpdatePost(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self,request,postId):
        data = request.data
        post = Post.objects.get(id=postId)
        description = data.get('caption')
        post.description = description
        post.save()
        serializer = PostSerializer(post)
        time.sleep(1)
        return Response({"response":serializer.data})
    

class GetProfilePosts(APIView):
    def post(self,request):
        data = request.data
        user_id = data.get('user_id')
        user = User.objects.get(id=user_id)
        posts = Post.objects.filter(user=user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


