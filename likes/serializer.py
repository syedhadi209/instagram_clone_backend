from rest_framework import serializers
from .models import Likes


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['user']