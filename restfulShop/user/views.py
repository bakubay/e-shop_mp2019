from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
class UserListApiView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)

class UserApiView(generics.RetrieveAPIView):
    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        return User.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)


class UserCreateApiView(generics.CreateAPIView):
    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        return User.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)


class UserUpdateApiView(generics.UpdateAPIView):
    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        return User.objects.all()
    permission_classes = (IsAuthenticated, AllowAny)
