from django.contrib import admin
from students.models import studentProfile,CourseHistory
# Register your models here.
admin.site.register(CourseHistory)
admin.site.register(studentProfile)