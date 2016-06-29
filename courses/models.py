from django.db import models
from django.contrib.auth.models import User
from venues.models import CourseVenue
from django.utils.html import format_html
from django.db.models.signals import pre_save
from audit_log.models.fields import LastUserField
from audit_log.models.managers import AuditLog
import datetime

class Couch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_couch = models.BooleanField(default = False)

    audit_log = AuditLog()

    def __unicode__(self):
        return u"%s %s" %(self.user.first_name, self.user.last_name)

    def get_user_email(self):
        return self.user.email



class Category(models.Model):
    title = models.CharField(max_length = 80)
    color_code = models.CharField(max_length = 25, help_text = "Add HEXA code of the course color. Example fffff.", unique = True)
    created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
    active = models.BooleanField(default = True)

    audit_log = AuditLog()

    def __unicode__(self):
        return self.title

    def category_color(self):
        return format_html('<span style="color: #{};">#{}</span>',
            self.color_code,
            self.color_code
            )

    def category_color_code(self):
        return u"#" + self.color_code


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['updated_date']

class Course(models.Model):
    title = models.CharField(max_length = 255)
    created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
    course_description = models.TextField()
    couch = models.ForeignKey(Couch, blank = True, null = True, limit_choices_to={'is_couch': True})
    course_start_date = models.DateTimeField()
    course_end_date = models.DateTimeField()
    publish = models.BooleanField(default = True)
    registration_start_date = models.DateField()
    registration_end_date = models.DateField()
    open_registration = models.BooleanField(default = False)
    course_price = models.DecimalField(max_digits = 5, decimal_places = 2, help_text="Course price in 2 digits format. Example 23.45.", default = 0.00)
    notes = models.TextField(blank = True, null = True, help_text="Notes to the course, what to bring etc...")
    registration_form_link = models.URLField(blank = True, null = True)
    interested_form_link = models.URLField(blank = True, null = True)
    course_venue = models.ForeignKey(CourseVenue, default = 1)
    course_category = models.ForeignKey(Category, default = 2)

    audit_log = AuditLog()

    def __unicode__(self):
        return u"%s" %(self.title)

    def price(self):
        return '{} CZK'.format(self.course_price)




    class Meta:
        ordering = ['updated_date']
