from django.db import models
from django.contrib.auth.models import User
from venues.models import CourseVenue
from django.utils.html import format_html
from django.db.models.signals import pre_save

class Couch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_couch = models.BooleanField(default = False)

    def __unicode__(self):
        return u"%s %s" %(self.user.first_name, self.user.last_name)

def pre_save_couch_receiver(sender, instance, *args, **kwargs):
    password1 = "123456"
    password2 = "123456"
    if instance.user.password1 == None and instance.user.password2 == None:
        instance.user.password1 = password1
        instance.user.password2 = password2
    else:
        instance.user.password1 = password1
        instance.user.password2 = password2

pre_save.connect(pre_save_couch_receiver, sender = User)


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
    couch = models.ForeignKey(Couch, blank = True, null = True, limit_choices_to={'is_couch': True})
    course_start_date = models.DateTimeField()
    course_end_date = models.DateTimeField()
    publish = models.BooleanField(default = True)
    registration_start_date = models.DateField()
    registration_end_date = models.DateField()
    open_registration = models.BooleanField(default = False)
    course_price = models.DecimalField(max_digits = 5, decimal_places = 2, help_text="Course price in 2 digits format. Example 23.45.")
    notes = models.TextField(blank = True, null = True, help_text="Notes to the course, what to bring etc...")
    registration_form_link = models.URLField(blank = True, null = True)
    course_venue = models.ForeignKey(CourseVenue, default = 1)
    course_category = models.ForeignKey(Category, default = 2)

    def __unicode__(self):
        return u"%s - %s" %(self.title, self.course_venue.city)

    def price(self):
        return '{} CZK'.format(self.course_price)

    class Meta:
        ordering = ['updated_date']
