from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginUserSerializer
from rest_framework import status,permissions
from rest_framework.exceptions import ValidationError
import time
from django.contrib.auth import authenticate,get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
User = get_user_model()

# Create your views here.
class RegisterUser(APIView):
    def post(self,request):
        data =request.data
        email = data.get('email')
        username = data.get('username')
        first_name = data.get('first_name')
        password = data.get('password')
        print(password)

        user = User.objects.filter(username=username)
        print(user)

        if not user:
            print('here')
            user = User.objects.create(
            username=username,
            first_name=first_name,
            email = email
            )
            user.set_password(password)
            user.save() 
            serializer = RegisterSerializer(user)   
            time.sleep(3)
            return Response(serializer.data)
        else:
            return Response({"error": "Username Already Taken"})
        
    

class LoginUser(APIView):
    def post(self,request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        serializer = LoginUserSerializer(user)
        if user:
            refresh = RefreshToken.for_user(user=user)
            time.sleep(2)
            return Response({"refresh":str(refresh), "access": str(refresh.access_token), "user":serializer.data})
        else:
            return Response({"error": "Invalid Credentials"})
        

class GetUserData(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        user = request.user
        serializer = LoginUserSerializer(user)
        return Response(serializer.data)


