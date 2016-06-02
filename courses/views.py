from django.shortcuts import render
from .serializers import CategorySerializer, CourseSerializer, CourseDetailSerializer
from .models import Course, Category
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication
from drf_multiple_model.views import MultipleModelAPIView
import datetime



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

class CourseRetrieveAPIView(generics.RetrieveAPIView):
	authentication_classes = [BasicAuthentication, ]
	permissions_classes = [permissions.IsAuthenticated, ]
	queryset = Course.objects.filter(publish = True)
	serializer_class = CourseDetailSerializer

class CategoryListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication, ]
    permissions_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        timestamp = self.kwargs['timestamp']
        queryset = Category.audit_log.filter(action_date__gte = timestamp).order_by('-id').distinct('id')
        return queryset

    serializer_class = CategorySerializer
