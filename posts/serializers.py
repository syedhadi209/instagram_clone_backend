from rest_framework import serializers
from .models import Post, Attachements
from authentication.serializers import LoginUserSerializer
from likes.serializer import LikeSerializer
from comments.serializers import CommentSerializer



class AttachementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachements
        fields = ['url','post']


class PostSerializer(serializers.ModelSerializer):
    user = LoginUserSerializer()
    attachements = AttachementSerializer(many=True)
    likes = LikeSerializer(many=True)
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ['id','description', 'attachements','user','likes','comments']