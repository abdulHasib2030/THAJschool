from django.db import models
# from django.contrib.auth.models import User
from accounts.models import Teacher
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Department(models.Model):
  department_name = models.CharField(max_length=100)
  slug = models.SlugField(unique=True)
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.department_name)
    super(Department, self).save(*args, **kwargs)
  def __str__(self):
      return self.department_name
  def get_url(self):
    return reverse('department_page', args=[self.slug])
  
  
class addCourses(models.Model):
  user = models.ForeignKey(Teacher, related_name='account', on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  slug = models.SlugField(unique=True)
  description = models.TextField(max_length=1000)
  
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  
  created_date = models.DateTimeField(auto_now_add=True)
  modified_date = models.DateTimeField(auto_now=True)
  available_courses= models.BooleanField(default=True)
  price = models.IntegerField()
  course_duration = models.CharField(max_length=50)
  course_content = models.TextField(max_length=2000)
  img = models.ImageField(upload_to='images/', blank =True)
  video = models.FileField(upload_to='teacher/course-video/', blank=True)
  
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title+ str(self.created_date))
    super(addCourses, self).save(*args, **kwargs)
      
  

  

