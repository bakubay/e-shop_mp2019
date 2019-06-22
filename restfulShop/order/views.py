from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics



# Create your views here.
class OrderApiView(generics.RetrieveAPIView):
    def get_serializer_class(self):
        return OrderSerializer

    def get_queryset(self):
        return Order.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)


class OrderCreateApiView(generics.CreateAPIView):
    def get_serializer_class(self):
        return OrderSerializer

    def get_queryset(self):
        return Order.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)


class OrderUpdateApiView(generics.UpdateAPIView):
    def get_serializer_class(self):
        return OrderSerializer
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_queryset(self):
        return Order.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)
