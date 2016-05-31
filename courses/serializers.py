from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Course, Category
from venues.serializers import CitySerializer

class CourseSerializer(serializers.ModelSerializer):
    course_venue = CitySerializer(many = False, read_only = True)
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'course_start_date',
            'course_end_date',
            'course_description',
            'course_venue',
            'updated_date',
        )

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    course_set = CourseSerializer(many = True, read_only = True)
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'color_code',
            'course_set',
        )
