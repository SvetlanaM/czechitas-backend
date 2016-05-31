from django.shortcuts import render
from .serializers import CategorySerializer, CourseSerializer
from .models import Course, Category
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication


class PreparedCourseListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication, ]
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = Course.objects.filter(publish = True, open_registration = False)
    serializer_class = CategorySerializer
