from django.urls import path
from teachers.views import TeacherView,TeacherDetailView

urlpatterns = [
    path('', TeacherView.as_view(), name='teachers'),  
    path('teachers/<int:pk>',TeacherDetailView.as_view(), name='teacher_detail'),  
]