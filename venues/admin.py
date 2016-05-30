from django.contrib import admin
from .models import CourseVenue

class VenueAdmin(admin.ModelAdmin):
    list_display = ('title', ('street_name', 'street_number'), 'city', 'active', )
    date_hierarchy = ['updated_date']
    list_editable = ('street_name', 'street_number', 'city', )
    search_fields = ('title',)
    list_filter = ('active', 'city', )

admin.site.register(CourseVenue, VenueAdmin)
