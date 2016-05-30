from django.db import models

class CourseVenue(models.Model):
    title = models.CharField(max_length = 255)
    created_date = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_date = models.DateTimeField(auto_now_add = False, auto_now = True)
    active = models.BooleanField(default = True)
    street_name = models.CharField(max_length = 255)
    street_number = models.CharField(max_length = 25)
    city = models.CharField(max_length = 25)

    def __str__(self):
        return u"%s - %s" %(self.title, self.city)

    class Meta:
        ordering = ['updated_date']
