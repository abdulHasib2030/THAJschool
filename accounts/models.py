from django.db import models
import django
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

class UserAccountManager(BaseUserManager):
	def create_user(self, first_name, last_name, username, email, password = None):
		if not email or len(email) <= 0 :
			raise ValueError("Email field is required !")
		if not password :
			raise ValueError("Password is must !")
    # if not username:
    #   raise ValueError("User must have an username")
		
		user = self.model(
			email = self.normalize_email(email) ,
      username = username,
      first_name = first_name,
      last_name = last_name,
		)
		user.set_password(password)
		user.save(using = self._db)
		return user
	
	def create_superuser(self, first_name, last_name, email, username, password):
		user = self.create_user(
			email = self.normalize_email(email) ,
			username= username,
      password= password,
      first_name=first_name,
      last_name=last_name,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using = self._db)
		return user
	
class UserAccount(AbstractBaseUser):
  class Types(models.TextChoices):
        STUDENT = "STUDENT" , "student"
        TEACHER = "TEACHER" , "teacher"
          
  type = models.CharField(max_length = 8 , choices = Types.choices , default = Types.TEACHER)
  first_name = models.CharField(max_length=50, null=True)
  last_name = models.CharField(max_length=50, null=True)
  username = models.CharField(max_length=50, unique=True, null=True)
  phone_number = models.CharField(max_length=50, null=True)
  email = models.EmailField(max_length=100, unique=True)
  image = models.ImageField(upload_to = 'images/account/', null=False, blank = False, default='images/account/profile.jpg')
  
  def get_img(self):
    return self.image.url
  
  # required
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now=True, null=True)
  is_active = models.BooleanField(default = True)
  is_staff = models.BooleanField(default = False)
  is_superuser = models.BooleanField(default = False)
  is_admin = models.BooleanField(default= False)
  is_student = models.BooleanField(default = False)
  is_teacher = models.BooleanField(default = False)
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  objects = UserAccountManager()
 
  def __str__(self):
    return str(self.email)
  def has_perm(self , perm, obj = None):
    return self.is_admin
  def has_module_perms(self , app_label):
    return True
  
  def save(self , *args , **kwargs):
    if not self.type or self.type == None :
      self.type = UserAccount.Types.TEACHER
    return super().save(*args , **kwargs)



class StudentManager(models.Manager):
	def create_user(self, first_name, last_name, username, email, password = None):
		if not email or len(email) <= 0 :
			raise ValueError("Email field is required !")
		if not password :
			raise ValueError("Password is must !")
 
		email = email.lower()
		user = self.model(
			email = email,
      username = username,
      first_name = first_name,
      last_name = last_name,
      
		)
		user.set_password(password)
		user.save(using = self._db)
		return user
	
	def get_queryset(self , *args, **kwargs):
		queryset = super().get_queryset(*args , **kwargs)
		queryset = queryset.filter(type = UserAccount.Types.STUDENT)
		return queryset	
		
class Student(UserAccount):
	class Meta :
		proxy = True
	objects = StudentManager()
	
	def save(self , *args , **kwargs):
		self.type = UserAccount.Types.STUDENT
		self.is_student = True
		return super().save(*args , **kwargs)
	
class TeacherManager(models.Manager):
	def create_user(self, first_name, last_name, username, email, password = None):
		if not email or len(email) <= 0 :
			raise ValueError("Email field is required !")
		if not password :
			raise ValueError("Password is must !")
		email = email.lower()
		user = self.model(
			email = email,
      username = username,
      first_name = first_name,
      last_name = last_name,
		)
		user.set_password(password)
		user.save(using = self._db)
		return user
		
	def get_queryset(self , *args , **kwargs):
		queryset = super().get_queryset(*args , **kwargs)
		queryset = queryset.filter(type = UserAccount.Types.TEACHER)
		return queryset
	
class Teacher(UserAccount):
	class Meta :
		proxy = True
	objects = TeacherManager()
	
	def save(self , *args , **kwargs):
		self.type = UserAccount.Types.TEACHER
		self.is_teacher = True
		return super().save(*args , **kwargs)
