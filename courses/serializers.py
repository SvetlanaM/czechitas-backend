from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Course, Category, Couch
from venues.serializers import CitySerializer, CourseVenueSerializer
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
    dates = serializers.SerializerMethodField()

    def get_dates(self, obj):
        temp = Category.objects.get(id=obj.id).audit_log.all()
        for i in temp:
            return i.action_date

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'color_code',
            'dates',
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
    course_venue = CourseVenueSerializer(many = False, read_only = True)
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
