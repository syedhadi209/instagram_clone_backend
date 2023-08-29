from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import Follow
from .serializer import FollowSerializer,UserIdSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class FollowUser(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,followingUserId):
        user = request.user
        following = User.objects.get(id=followingUserId)
        isFollow = Follow.objects.filter(user_id=user, followers = following)
        if isFollow:
            isFollow.delete()
            return Response({'response':0})
        else:
            follow = Follow.objects.create(user_id=user, followers=following)
            serializer = FollowSerializer(follow)
            return Response({"response":serializer.data})
        


class GetFollowRequests(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        user = request.user
        followers = Follow.objects.filter(followers=user)
        serializer = UserIdSerializer(followers, many=True)
        return Response(serializer.data)
    

class AcceptFollowRequest(APIView):
    def post(self,request, requestId):
        request = Follow.objects.get(id=requestId)
        request.accepted = True
        request.save()
        return Response({'response': 'ok'})


# class AcceptFollowRequest(APIView):

