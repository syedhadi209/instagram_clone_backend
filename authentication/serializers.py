from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from followers.serializer import FollowSerializer,UserIdSerializer
from comments.serializers import CommentSerializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    

class FollowUserSerializer(serializers.ModelSerializer):
    following = FollowSerializer(many=True)
    followers = UserIdSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'following', 'followers' ]


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name', "email","profile_picture"]


class UserProfileSerializer(serializers.ModelSerializer):
    following = FollowSerializer(many=True)
    followers = UserIdSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture', 'following', 'followers']