from django.conf.urls import include, url
from django.contrib import admin
from venues.views import CourseVenueListAPIView, CityListAPIView
from courses.views import PreparedCourseListAPIView, OpenCourseListAPIView, CourseAllAPIView, CategoryListAPIView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/venues/$', CourseVenueListAPIView.as_view(), name='venue-list'),
    url(r'^api/v1/update-from=(?P<timestamp>\d*[.]?\d+)/$', CategoryListAPIView.as_view(), name='update-list'),
    url(r'^api/v1/cities/$', CityListAPIView.as_view(), name='city-list'),
    url(r'^api/v1/courses/prepared/$', PreparedCourseListAPIView.as_view(), name='course-prepared-list'),
    url(r'^api/v1/courses/open/$', OpenCourseListAPIView.as_view(), name='course-open-list'),
    url(r'^api/v1/courses/all/$', CourseAllAPIView.as_view(), name='course-all-list'),
    url(r'^api/docs/', include('rest_framework_swagger.urls')),

]
