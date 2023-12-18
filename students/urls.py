from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mainPageView, name = 'main_page'),
    path('department/<slug:slug_department>/', views.mainPageView, name = 'department_page'),
    
    path('single_page/<slug:title_slug>/', views.singleCoursePageView, name = 'single_page'),
    path('search/', views.search, name = 'search'),
    
    ############ student account register login profile ###########
    path('register/', views.studentRegisterView, name = 'student_register'),
    path('login/', views.studentLoginView, name = 'student_login'),
    path('logout/', views.studentLogout, name = 'student_logout'),
    
    path('profile/', views.studentAccountupdate.as_view(), name = 'student_profile'),
    # path('student-profile/', views.accountSettings, name = 'student_profile'),
    path('address/', views.studentAddress.as_view(), name = 'student_address'),
    path('education/', views.studentEducation.as_view(), name = 'student_education'),
    path('history/<int:id>/', views.courseHistory, name = 'course_history'),
    path('certificate/<int:id>/', views.courseCertificate, name = 'certificate')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


