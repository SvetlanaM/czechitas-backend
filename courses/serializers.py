from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Course, Category, Couch
from venues.serializers import CitySerializer
from django.contrib.auth.models import User

class UserDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='get_user_email')
    class Meta:
        model = Couch
        fields = [
        'id',
         'user',
		]

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
    url = serializers.HyperlinkedIdentityField(view_name = 'course-detail', lookup_field = 'pk')
    class Meta:
        model = Course
        fields = (
            'id',
            'url',
            'title',
            'course_start_date',
            'course_end_date',
            'course_description',
            'course_venue',
            'updated_date',
            'course_category',

        )

class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
    course_category = CategorySerializer(many = False, read_only = True)
    course_venue = CitySerializer(many = False, read_only = True)
    couch = UserDetailSerializer(many = False, read_only = True)
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'course_description',
            'course_start_date',
            'course_end_date',
            'course_price',
            'notes',
            'registration_form_link',
            'course_venue',
            'course_category',
            'couch',
        )
