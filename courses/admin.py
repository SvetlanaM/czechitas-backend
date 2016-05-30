from django.contrib import admin
from .models import Course, Category

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'open_registration', 'category', 'venue', 'course_price', 'couch_email', )
    list_filter = ('publish', 'course_start_date', 'registration_start_date', 'open_registration', )
    list_editable = ('course_price', 'couch_email', )
    search_fields = ('title', )

    def save(self, request, obj, *args, **kwargs):
        obj.course_admin = request.user.id
        obj.save()

    def category(self, obj):
        return obj.course_category.title

    def venue(self, obj):
        return obj.course_venue.title

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'category_color', )
    list_filter = ('active', )
    list_editable = ['title']
    search_fields = ('title',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
