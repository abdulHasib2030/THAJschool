from django import forms
from accounts.models import *


class teacherRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class':'form-control',}))
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirm Password'
  }))
  
  class Meta:
    model = Teacher
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
  
  def clean(self):
    cleaned_data = super(teacherRegistrationForm, self).clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    
    if password != confirm_password:
      raise forms.ValidationError(
        "Password does not match!"
      )
  def __init__(self, *args, **kwargs):
    super(teacherRegistrationForm, self).__init__(*args, **kwargs)
    
    self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First name'
    self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last name'
    self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone number'
    self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
    
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'form-control'
      
class studentRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class':'form-control',}))
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirm Password'
  }))
  
  class Meta:
    model = Student
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
  
  def clean(self):
    cleaned_data = super(studentRegistrationForm, self).clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    
    if password != confirm_password:
      raise forms.ValidationError(
        "Password does not match!"
      )
  def __init__(self, *args, **kwargs):
    super(studentRegistrationForm, self).__init__(*args, **kwargs)
    
    self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First name'
    self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last name'
    self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone number'
    self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
    
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'form-control'
