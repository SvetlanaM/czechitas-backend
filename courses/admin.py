from django.contrib import admin
from .models import Course, Category

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_start_date', 'publish', 'registration_start_date', 'category_title','venue_title', )
    list_filter = ('title', 'publish', 'course_start_date', )
    list_editable = ('course_start_date', 'publish', 'registration_start_date', )
    search_fields = ('title', )

    def save(self, request, obj, change):
        obj.course_admin = request.user
        obj.save()

    def category_title(self, obj):
        return obj.course_category.title

    def venue_title(self, obj):
        return obj.course_venue.title

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'category_color', )
    list_filter = ('active', )
    list_editable = ['title']
    search_fields = ('title',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
