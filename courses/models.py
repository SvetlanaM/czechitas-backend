from django.db import models
from django.contrib.auth.models import User
from venues.models import CourseVenue
from django.utils.html import format_html

class Category(models.Model):
    title = models.CharField(max_length = 80)
    color_code = models.CharField(max_length = 25, help_text = "Add HEXA code of the course color. Example fffff.", unique = True)
    created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
    active = models.BooleanField(default = True)

    def __str__(self):
        return self.title

    def category_color(self):
        return format_html('<span style="color: #{};">#{}</span>',
            self.color_code,
            self.color_code
            )


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['updated_date']

class Course(models.Model):
    title = models.CharField(max_length = 255)
    created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
    course_description = models.TextField()
    course_admin = models.ForeignKey(User, blank = True, null = True, help_text="Automatic preffiled by currently log in user.")
    course_start_date = models.DateTimeField()
    course_end_date = models.DateTimeField()
    publish = models.BooleanField(default = True)
    registration_start_date = models.DateField()
    registration_end_date = models.DateField()
    open_registration = models.BooleanField(default = False)
    course_price = models.DecimalField(max_digits = 5, decimal_places = 2, help_text="Course price in 2 digits format. Example 23.45.")
    couch_email = models.EmailField(max_length=125, blank = True, null = True)
    notes = models.TextField(blank = True, null = True, help_text="Notes to the course, what to bring etc...")
    registration_form_link = models.URLField(blank = True, null = True)
    course_venue = models.ForeignKey(CourseVenue, default = 1)
    course_category = models.ForeignKey(Category, default = 2)

    def __unicode__(self):
        return u"%s - %s" %(self.title, self.course_venue.city)

    def save(self, *args, **kwargs):
        self.course_admin = request.user.id
        self.course_admin.save()

    class Meta:
        ordering = ['updated_date']
