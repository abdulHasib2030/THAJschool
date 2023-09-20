from django.contrib import admin
from accounts.models import *
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(Teacher)
admin.site.register(Student)