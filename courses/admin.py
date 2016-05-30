from django.contrib import admin
from .models import Course, Category, Couch
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CouchInline(admin.StackedInline):
    model = Couch

class CouchAdmin(BaseUserAdmin):
    inlines = (CouchInline, )

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'couch', 'category', 'venue', 'price',  )
    list_filter = ('publish', 'course_start_date', 'registration_start_date', 'open_registration', )
    search_fields = ('title', )


    def category(self, obj):
        return obj.course_category.title

    def venue(self, obj):
        return obj.course_venue.title

    def couch(self, obj):
        return u" %s %s" %(obj.couch.first_name, obj.couch.last_name)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'category_color', )
    list_filter = ('active', )
    list_editable = ['title']
    search_fields = ('title',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(User)
admin.site.register(User, CouchAdmin)
