from django.conf.urls import include, url
from django.contrib import admin
from venues.views import CourseVenueListAPIView
from courses.views import PreparedCourseListAPIView, OpenCourseListAPIView

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/venues/$', CourseVenueListAPIView.as_view(), name='venue-list'),
    url(r'^api/v1/courses/prepared/$', PreparedCourseListAPIView.as_view(), name='course-prepared-list'),
    url(r'^api/v1/courses/open/$', OpenCourseListAPIView.as_view(), name='course-open-list'),

]
