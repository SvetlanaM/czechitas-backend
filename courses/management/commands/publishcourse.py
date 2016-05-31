from django.core.management.base import BaseCommand, CommandError
from courses.models import Course
from django.utils import timezone
import datetime

class Command(BaseCommand):


    def handle(self, *args, **options):
        courses = Course.objects.all()
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        for c in courses:
            try:
                course = Course.objects.get(pk=int(c.pk))
                if str(course.registration_start_date) == today:
                    course.open_registration = True
                    print ("Changed")
                    course.save()
                else:
                    print("No changes")
                    print (course.registration_start_date)
                    print (today)
            except Course.DoesNotExist:
                raise CommandError("Error")
