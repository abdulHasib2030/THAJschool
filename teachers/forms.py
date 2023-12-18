
from django import forms
from .models import addCourses
from accounts.models import Teacher
 

########## Add courses Form ################# 
class addCoursesForm(forms.ModelForm):
  class Meta:
    model = addCourses
    fields = ['title', 'description', 'department', 'available_courses', 'price', 'course_duration', 'course_content', 'img', 'video', 'course_video']
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
        
    for field in self.fields:
      if field == 'available_courses':
        
        print()
        continue
      
      
        
      self.fields[field].widget.attrs.update({
      'class' : (
          'form-control'
      )   
  })
     
########## Update Teacher Account Form ##############
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = [ 'image',  'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'form-control'
                )
            })
        # jodi user er account thake 
        

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     if commit:
    #         user.save()

    #     return user
    



