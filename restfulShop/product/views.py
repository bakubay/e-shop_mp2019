from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *



# Create your views here.
class ProductListApiView(generics.ListAPIView):
    def get_serializer_class(self):
        return ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)


class ProductCreateApiView(generics.CreateAPIView):
    def get_serializer_class(self):
        return ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)


class ProductApiView(generics.RetrieveAPIView):
    def get_serializer_class(self):
        return ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)


class ProductUpdateApiView(generics.UpdateAPIView):
    def get_serializer_class(self):
        return ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)


class ProductDestroyApiView(generics.DestroyAPIView):
    def get_serializer_class(self):
        return ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)


class CategoryCreateApiView(generics.CreateAPIView):
    def get_serializer_class(self):
        return CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)


class CategoryViewApiView(generics.RetrieveAPIView):
    def get_serializer_class(self):
        return CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)


class CategoryListApiView(generics.ListAPIView):
    def get_serializer_class(self):
        return CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
        permission_classes = (IsAuthenticated, AllowAny)

