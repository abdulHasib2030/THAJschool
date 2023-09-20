from .models import addCourses, Department
from accounts.models import UserAccount

def menu_links(request):
  links = Department.objects.all()
  return dict(links = links)

