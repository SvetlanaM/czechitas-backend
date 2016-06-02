from django.shortcuts import render
from .serializers import CategorySerializer, CourseSerializer, CourseDetailSerializer, DeletedSerializer
from .models import Course, Category
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication
from drf_multiple_model.views import MultipleModelAPIView
import datetime, pytz, timedelta
from venues.models import CourseVenue
from venues.serializers import CitySerializer, CourseVenueSerializer



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

class CategoryListAPIView(MultipleModelAPIView):
    authentication_classes = [BasicAuthentication, ]
    permissions_classes = [permissions.IsAuthenticated, ]

    def get_queryList(self):
        timestamp = float(self.kwargs['timestamp'])
        date_value = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S%Z') - timedelta(hours = 2)
        

        queryList = (
            (Category.objects.filter(updated_date__gte = date_value).order_by('updated_date').distinct(), CategorySerializer, 'categories'),
            (Course.objects.filter(updated_date__gte = date_value).order_by('updated_date').distinct(), CourseDetailSerializer, 'courses'),
            (CourseVenue.objects.filter(updated_date__gte = date_value).order_by('updated_date').distinct(), CourseVenueSerializer, 'venues'),
            (CourseVenue.objects.filter(updated_date__gte = date_value).order_by('updated_date').distinct(), CitySerializer, 'cities'),
            (Course.audit_log.filter(action_date__gte = date_value, action_type = "D").order_by('action_date').distinct(), DeletedSerializer, 'deleted-courses')
        )

        return queryList
