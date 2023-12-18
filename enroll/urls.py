from django.urls import path
from enroll.views import *

urlpatterns = [
    path('<int:course_id>/', CoursEnrollView, name = 'enroll'),
]
