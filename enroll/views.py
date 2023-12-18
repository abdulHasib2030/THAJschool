from django.shortcuts import render, redirect
from enroll.models import *
from teachers.models import addCourses
# Create your views here.

def CoursEnrollView(request, course_id):
  # if request.method == 'POST':
    course_name = addCourses.objects.get(id=course_id)
    enroll = CourseEnroll.objects.create(student=request.user, course=course_name, course_access=True)

    enroll.save()
    return redirect('main_page')
  
  # return redirect('main_page')
  