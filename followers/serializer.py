from rest_framework import serializers
from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['followers']


class UserIdSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    class Meta:
        model = Follow
        fields = ['id','user_id','accepted']

    
    def get_user_id(self,obj):
        user_data = {
            'id':obj.user_id.id,
            'username': obj.user_id.username,
        }
        return user_data