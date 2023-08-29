from rest_framework import serializers
from .models import Story,StoryAttachement


class AttachementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryAttachement
        fields = "__all__"


class StorySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    urls = AttachementSerializer(many=True)
    class Meta:
        model = Story
        fields = ['id','user', 'time_stamp','urls']


    def get_user(self,obj):
        user_data = {
            'id': obj.user.id,
            'username': obj.user.username
        }
        return user_data