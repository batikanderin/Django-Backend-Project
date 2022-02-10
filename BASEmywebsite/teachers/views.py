from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from teachers.models import Teacher
from courses.models import Course

# Create your views here.

class TeacherView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses']=Course.objects.filter(available=True, teachers= self.kwargs['pk'])        
        return context
