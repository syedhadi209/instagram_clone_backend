from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = "__all__"


    def get_user(self,obj):
        user_data = {
            'id':obj.user.id,
            'username': obj.user.username,
            'profile_picture': obj.user.profile_picture,
        }
        return user_data