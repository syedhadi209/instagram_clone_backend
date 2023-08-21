from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', "email","profile_picture"]