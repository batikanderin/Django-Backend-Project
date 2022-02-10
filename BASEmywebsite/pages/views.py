from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from courses.models import Course
from pages.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from teachers.models import Teacher


# Create your views here.

# def index(request):
#     return render(request,'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses']=Course.objects.filter(available=True)[:2]
        context['courses_count']=Course.objects.filter(available=True).count()
        context['total_student']=User.objects.count()
        context['total_teachers']=Teacher.objects.count()
        return context




# def about(request):
#     return render(request,'about.html')

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(SuccessMessageMixin,FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url=reverse_lazy('contact')
    success_message='We Received Your Message'


    #formu kaydedip databaseye gonderdik
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)