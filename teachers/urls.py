from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('register/', views.register, name = 'register'),
    
    path('login/', views.login, name = 'login'),
    path('dashboard/', views.profile, name = 'profile'),
    path('logout/', views.logout, name = 'logout'),
    path('add_course/', views.teacherAddcourses, name = 'add_course'),
    path('success/', views.success, name = 'success' ),
    path('edit_page/', views.EditPageCourses, name = 'edit_page'),
    path('update_course/<int:id>/', views.updateCourses, name = 'update_course'),
    path('delete_course/<int:id>/', views.deleteCourse, name = 'delete_course'),
    
    path('user-profile/', views.teacherAccountupdate.as_view(), name = 'user_profile')
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



