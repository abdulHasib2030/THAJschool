from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import teacherRegistrationForm
from accounts.models import Teacher
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from .forms import addCoursesForm, UserUpdateForm
from .models import addCourses


# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
########### Register Teacher Account ############
def register(request):
  if request.method == 'POST':
    form = teacherRegistrationForm(request.POST)
    if form.is_valid():
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      phone_number = form.cleaned_data['phone_number']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      username = email.split('@')[0]
      
      user = Teacher.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
      
      user.phone_number = phone_number
      user.save()
      auth.login(request, user)
      return redirect('profile')
  else:
    form = teacherRegistrationForm()
  context = {
    'form':form,
  }
  return render(request, 'newregister.html', context)

########### Login Teacher Account ############
def login(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    
    user = auth.authenticate(email=email, password = password)
    if user is not None:
      if user.is_teacher == True:
        auth.login(request, user)
       
        return redirect('profile')
      else:
        messages.success(request, 'You are not register Teacher.')
        return redirect('login')
    else:
      messages.success(request, 'Invalid login credentials')
      return redirect('login')
  return render(request, 'newlogin.html')

########### logout Teacher Account ############
@login_required(login_url='login')
def logout(request):
  auth.logout(request)
  messages.success(request, 'Your are logged out.')
  return redirect('login')
  
########### Profile Teacher Account ############
@login_required(login_url='login')
def profile(request):
  return render(request, 'profile.html')

############ Teacher add Courses ###############
def teacherAddcourses(request): 
  if request.method == 'POST':
    form = addCoursesForm(request.POST, request.FILES)
    if form.is_valid():
      # form.save()
      order = form.save(commit=False)
      order.user = request.user
      order.save()
      return redirect('edit_page')
  else:
    form = addCoursesForm()
  return render(request, 'add_courses.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')

############ Teacher edit Courses ###############
def EditPageCourses(request):
  context = addCourses.objects.filter(user = request.user)
  return render(request, 'edit_courses.html', {'context':context})

############ Teacher update Courses ###############
def updateCourses(request, id):
  task = addCourses.objects.get(pk=id)
  form = addCoursesForm(instance = task)
  if request.method == 'POST':
    form = addCoursesForm(request.POST, request.FILES, instance = task)
    if form.is_valid():
      form.save()
      return redirect('edit_page')
  return render(request, 'update_courses.html', {'form':form})

  
############ Teacher delete Courses ###############
def deleteCourse(request, id):
  department = addCourses.objects.get(pk=id).delete()
  return redirect('edit_page')

########### Account Update  ##########
class teacherAccountupdate(View):
  template_name = 'user_profile.html'
  
  def get(self, request):
    form = UserUpdateForm(instance = request.user)
    return render(request, self.template_name, {'form':form})
  
  def post(self, request):
    
    form =UserUpdateForm(request.POST, request.FILES, instance = request.user)
    if form.is_valid():
      form.save()
      return redirect('profile')
      
    return render(request, self.template_name, {'form':form})





