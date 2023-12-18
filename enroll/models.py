from django.db import models
from accounts.models import Student
from teachers.models import addCourses

# Create your models here.
class CourseEnroll(models.Model):
  student = models.ForeignKey(Student, related_name='student_name', on_delete=models.CASCADE, null=True)
  course = models.ForeignKey(addCourses, related_name='course_name', on_delete=models.CASCADE, null=True)
  course_access = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
      return self.course.title
  
  
  


