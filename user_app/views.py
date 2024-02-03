from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
# Create your views here.

class UserCreationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # Using create() method = it will create a user but password will be not hashed! But access token will generate or
    # it will work onlly if we use create() method below class Meta in serializers.py
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() # will trigger create() method in serializers.py

        # Generate JWT tokens for the newly created user/ also it can be given while login
        # refresh = RefreshToken.for_user(user)
        # access_token = str(refresh.access_token)
        return Response({'message': 'User created successfully!', 'Data': serializer.data}, status=status.HTTP_201_CREATED)
    
    # Another way to create user
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        
    #     password = make_password(serializer.validated_data['password'])  # Hash the password
    #     username = serializer.validated_data.get('username')
    #     email = serializer.validated_data.get('email')
        
    #     if username and password and email:
    #         # Create the user with the hashed password
    #         user = User.objects.create(username=username, email=email, password=password)
    #     else:
    #         user = User.objects.create(username=username, password=password)
    #     return Response({'message': 'User created successfully!'}, status=status.HTTP_201_CREATED)

    # Using post method with APIView class, user will be created with username and password but withut email
    # def post(self, request, *args, **kwargs):
    #     serializer = UserSerializer(data=request.data)
        
    #     if serializer.is_valid():
    #         username = serializer.validated_data.get('username')
    #         password = serializer.validated_data.get('password')
    #         if username and password:
    #             user = User.objects.create(username=username)
    #             user.set_password(password)
    #             user.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

        
        
