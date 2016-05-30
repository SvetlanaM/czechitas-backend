from django.contrib import admin
from .models import Course, Category, Couch
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .forms import UserCreateForm

class UserAdmin(BaseUserAdmin):
    add_form = UserCreateForm

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2',  ),
        }),
    )

class CouchInline(admin.StackedInline):
    model = Couch

class CouchAdmin(BaseUserAdmin):
    inlines = (CouchInline, )

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'couch', 'category', 'venue', 'price',  )
    list_filter = ('publish', 'course_start_date', 'registration_start_date', 'open_registration', )
    search_fields = ('title', )
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(publish=False)
    make_published.short_description = "Mark selected stories as published"


    def category(self, obj):
        return obj.course_category.title

    def venue(self, obj):
        return "{} - {}".format(obj.course_venue.title, obj.course_venue.city)

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
#admin.site.register(User, CouchAdmin)
admin.site.register(User, UserAdmin)
