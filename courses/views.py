from django.shortcuts import render
from .serializers import CategorySerializer, CourseSerializer, CourseDetailSerializer, DeletedSerializer
from .models import Course, Category
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication
from drf_multiple_model.views import MultipleModelAPIView
import datetime, pytz
from datetime import timedelta
from venues.models import CourseVenue
from venues.serializers import CitySerializer, CourseVenueSerializer



class PreparedCourseListAPIView(generics.ListAPIView):
    permissions_classes = [permissions.AllowAny, ]
    queryset = Course.objects.filter(publish = True, open_registration = False).order_by('registration_start_date')
    serializer_class = CourseDetailSerializer


class OpenCourseListAPIView(generics.ListAPIView):
    permissions_classes = [permissions.AllowAny, ]
    queryset = Course.objects.filter(publish = True, open_registration = True).order_by('registration_start_date')
    serializer_class = CourseDetailSerializer

class CourseAllAPIView(generics.ListAPIView):
	permissions_classes = [permissions.AllowAny, ]
	queryset = Course.objects.filter(publish = True)
	serializer_class = CourseDetailSerializer

class CategoryListAPIView(generics.ListAPIView):
    permissions_classes = [permissions.AllowAny, ]

    def get_queryset(self):
        timestamp = float(self.kwargs['timestamp'])
        date_value = datetime.datetime.fromtimestamp(timestamp) - timedelta(hours = 2)
        date_value = date_value.strftime('%Y-%m-%dT%H:%M:%S%Z')
        queryset = Course.objects.filter(updated_date__gte = date_value).order_by('updated_date').distinct()
        return queryset
