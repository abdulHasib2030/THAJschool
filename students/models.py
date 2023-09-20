from django.db import models
from accounts.models import Student
from students.content import EDUCATION_LEVEL, PAYMENT_STATUS

class CourseHistory(models.Model):
  course_title = models.CharField(max_length=200)
  payment_method = models.CharField(max_length=100)
  enroll_date = models.DateField(auto_now_add=True)
  payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS)
  
  def __str__(self):
      return self.course_title
  

class studentProfile(models.Model):
  user = models.OneToOneField(Student, related_name='student_account', on_delete=models.CASCADE)
  student_img = models.ImageField(upload_to = 'images/student/profile/', null=True, blank= True)
  country = models.CharField(max_length=100, null=True, blank=True)
  city = models.CharField(max_length=150, null=True, blank= True)
  street_address = models.CharField(max_length=200, null=True, blank=True)
  education_level = models.CharField(max_length=200, choices=EDUCATION_LEVEL, null=True, blank=True)
  institute = models.CharField(max_length=150, null= True, blank=True)
  passing_year = models.DateField( null=True, blank= True)
  
  course_history = models.OneToOneField(CourseHistory, on_delete=models.CASCADE, null= True, blank=True)
  certificate = models.ImageField(upload_to='images/student/certificate/', blank=True)
  
  def __str__(self):
      return self.user.email
  
  
  