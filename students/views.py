from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views import View
from accounts.forms import studentRegistrationForm
from accounts.models import Student, Teacher
from teachers.models import addCourses, Department
from students.forms import studentUpdateProfileForm, studentAddressForm,studentEducateionForm,studentCourseHistoryForm
from students.models import CourseHistory
from enroll.models import CourseEnroll
############# Register Student Account ############
def studentRegisterView(request):
  if request.method == 'POST':
    form = studentRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      phone_number = form.cleaned_data['phone_number']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      username = email.split('@')[0]
     
      
      user = Student.objects.create_user( first_name=first_name, last_name=last_name, email=email, username=username, password=password)
      
      user.phone_number = phone_number
      user.save()
      
      login(request, user)
      return redirect('main_page')
  else:
    form = studentRegistrationForm()
  context = {
    'form':form,
  }
  
  return render(request, 'student_register.html', context)      


# Create your views here.
def mainPageView(request, slug_department=None):
  teacher = Teacher.objects.all()
  teacher_valid = True
  lst = []
  
  if len(teacher) > 4: 
    teacher_valid = False
    cnt = 0
    for i in teacher:
      if cnt == 4:
        break
      dic = {} 
      dic['first_name'] = i.first_name
      dic['last_name'] = i.last_name
   
      lst.append(dic)
      cnt += 1
  

  if slug_department != None:
    department = get_object_or_404(Department, slug =slug_department)
    course = addCourses.objects.filter(available_courses=True, department = department )
    p_count = course.count()
  
  else:
    course = addCourses.objects.filter(available_courses=True)
    p_count = course.count()
  
  if teacher_valid == True:
    teachers =  teacher
  else:
    teachers = lst
  context = {
    'course':course,
    'p_count':p_count,
    'teachers':teachers,
     
  }

  return render(request, 'main_page.html', context)


########### Single Course Page View ########
def singleCoursePageView(request, title_slug):
  context = addCourses.objects.get(slug=title_slug)   
  
  try:
    course_access = CourseEnroll.objects.get(student=request.user.id)
    course_access = True
  except CourseEnroll.DoesNotExist:
    course_access = False
  print(course_access)
  return render(request, 'single_page.html', {'context':context, 'course_access':course_access})

############## course Search ###########
def search(request):
  if 'keyword' in request.GET:
    keyword = request.GET['keyword']
    if keyword:
      course = addCourses.objects.order_by('-created_date').filter(Q(description__icontains = keyword) | Q(title__icontains = keyword), available_courses=True) 
      p_count = course.count()
    else:
      messages.success(request,'Invalid')
    context={
       'course':course,
       'p_count':p_count,  
    }
  return render(request, 'main_page.html', context)


      
############### Login Student Account #############
def studentLoginView(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    
    user = authenticate(email=email, password = password)
    
    if user is not None:
      if user.is_student == True:
        login(request, user)
        return redirect('main_page')
      else:
        messages.success(request,'You are not register Student.')
        return redirect('student_login')
    else:
      messages.success(request,'Invalid email or password')
      return redirect('student_login')
  return render(request, 'student_login.html')
    
############## Logout Student Account #############
def studentLogout(request):
  logout(request)
  return redirect('student_login')


########### student profile Account Update ##########
class studentAccountupdate(View):
  template_name = 'student_profile.html'
  
  def get(self, request):
    form = studentUpdateProfileForm(instance = request.user)
    return render(request, self.template_name, {'form':form})
  
  def post(self, request):
    form =studentUpdateProfileForm(request.POST, request.FILES, instance = request.user)
    if form.is_valid():
      form.save()
      
      return redirect('student_profile')
    return render(request, self.template_name, {'form':form})
    
############ Student Profile Address ###########
class studentAddress(View):
  template_name = 'student_address.html'
  
  def get(self, request):
    form = studentAddressForm(instance = request.user)
    return render(request, self.template_name, {'form':form})
  
  def post(self, request):
    form =studentAddressForm(request.POST, instance = request.user)
    if form.is_valid():
      form.save()
      return redirect('student_address')
      
    return render(request, self.template_name, {'form':form})
  
############ Student Profile  education###########
class studentEducation(View):
  template_name = 'student_education.html'
  
  def get(self, request):
    form = studentEducateionForm(instance = request.user)
    return render(request, self.template_name, {'form':form})
  
  def post(self, request):
    form =studentEducateionForm(request.POST, instance = request.user)
    if form.is_valid():
      form.save()
      return redirect('student_education')
      
    return render(request, self.template_name, {'form':form})


############ Student profile Course History ######
def courseHistory(request, id):
  # history = CourseHistory.objects.get(pk=id)
  # print(history)
  # form = studentCourseHistoryForm(instance = history)
  return render(request, 'student_course_history.html')

############ Student profile Course Certificate ######
def courseCertificate(request, id):
  return render(request, 'student_course_certificate.html')
 



