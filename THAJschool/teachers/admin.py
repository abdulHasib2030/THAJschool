from django.contrib import admin
from . import models

# Register your models here.
class CourcesModel(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)
                         }
  list_display = ['user', 'title', 'department', 'price', 'available_courses', 'modified_date', 'created_date']

class DepartmentModel(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('department_name',)}
  
admin.site.register(models.Department, DepartmentModel)
admin.site.register(models.addCourses, CourcesModel)

