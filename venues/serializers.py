from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import CourseVenue

class CitySerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.CharField(source='get_city')
    states = serializers.SerializerMethodField()
    def get_states(self, obj):
        temp = CourseVenue.objects.get(id=obj.id).audit_log.last()
        try:
            if temp.active == True:
                return temp.action_type
            elif temp.active == False:
                return "D"
            else:
                pass
        except:
            return "No changes"
    class Meta:
        model = CourseVenue
        fields = (
            'id',
            'city',
            'states',
        )

class CourseVenueSerializer(serializers.HyperlinkedModelSerializer):
    states = serializers.SerializerMethodField()

    def get_states(self, obj):
        temp = CourseVenue.objects.get(id=obj.id).audit_log.last()
        try:
            if temp.active == True:
                return temp.action_type
            elif temp.active == False:
                return "D"
            else:
                pass
        except:
            return "No changes"
    class Meta:
        model = CourseVenue
        fields = (
            'id',
            'title',
            'street_name',
            'street_number',
            'city',
            'states',
        )
