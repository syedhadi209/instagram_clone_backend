from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response
from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

class AddComment(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,postId):
        user = request.user
        data = request.data
        post = Post.objects.get(id=postId)
        content = data.get('content')
        comment = Comment.objects.create(content=content,user=user,post=post)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response({"response":serializer.data},status=status.HTTP_201_CREATED)
    

class DeleteComment(APIView):
    def delete(self,request, commentId):
        comment = Comment.objects.get(id=commentId)
        comment.delete()
        return Response({'response': 'comment deleted'}, status=status.HTTP_200_OK)
    

class UpdateComment(APIView):
    def put(self,request, commentId):
        data = request.data
        comment = Comment.objects.get(id=commentId)
        updatedContent = data.get('updatedContent')
        comment.content = updatedContent
        comment.save()
        serializer = CommentSerializer(comment)
        return Response({'response':serializer.data})

