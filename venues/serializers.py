from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import CourseVenue

class CitySerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.CharField(source='get_city')
    class Meta:
        model = CourseVenue
        fields = (
            'id',
            'city',
        )

class CourseVenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseVenue
        fields = (
            'id',
            'title',
            'street_name',
            'street_number',
            'city',
        )
