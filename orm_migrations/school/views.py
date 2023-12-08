from django.views.generic import ListView
from .models import Student

class StudentsListView(ListView):
    model = Student
    template_name = 'school/students_list.html'
    context_object_name = 'object_list'
    ordering = ['group']
