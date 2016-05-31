from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Course, Category
from venues.serializers import CitySerializer

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'color_code',
        )

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    course_category = CategorySerializer(many = False, read_only = True)
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
            'course_category',
        )
