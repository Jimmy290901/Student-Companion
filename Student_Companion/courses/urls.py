
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('addCourse', addCourse),
    path('addFaculty',addFaculty),
    path('myCourses', listCourses, name='listCourses'),
    path('allotCategory/<slug:course_ID>/<slug:person_ID>', allotCategory, name='allotCategory'),
    path('<slug:course_ID>', displayCourse, name="displayCourse"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)