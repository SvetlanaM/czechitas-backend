from django.shortcuts import render
from .serializers import CategorySerializer, CourseSerializer
from .models import Course, Category
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication


class PreparedCourseListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication, ]
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Course.objects.filter(publish = True, open_registration = False).order_by('updated_date')
    serializer_class = CourseSerializer


class OpenCourseListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication, ]
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Course.objects.filter(publish = True, open_registration = True).order_by('updated_date')
    serializer_class = CourseSerializer

class CategoryListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication, ]
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Category.objects.filter(active = True)
    serializer_class = CategorySerializer
