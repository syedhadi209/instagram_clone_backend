from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from posts.models import Post
from rest_framework.response import Response
from .models import Likes
from .serializer import LikeSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

class LikePost(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self,request,postId,userId):
        user = User.objects.get(id=userId)
        post = Post.objects.get(id=postId)
        isLike = Likes.objects.filter(user=user, post=post)
        if isLike:
            isLike.delete()
            return Response({"response": 0})
        else:
            like = Likes.objects.create(user=user, post=post)
            return Response({"response": 1})

        

class GetLikes(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request,postId):
        likes = Likes.objects.filter(post_id = postId)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

