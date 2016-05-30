from django.contrib import admin
from .models import Course, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', )
    #list_filter = ('active')
    list_editable = ('title')
    search_fields = ['title']

admin.site.register(Course)
admin.site.register(Category, CategoryAdmin)
