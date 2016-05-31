from django.shortcuts import render
from .serializers import CourseVenueSerializer, CitySerializer
from .models import CourseVenue
from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication

class CourseVenueListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication, ]
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = CourseVenue.objects.filter(active = True)
    serializer_class = CourseVenueSerializer

class CityListAPIView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication, ]
    permissions_classes = [permissions.IsAuthenticated, ]
    queryset = CourseVenue.objects.filter(active = True)
    serializer_class = CitySerializer
