from django.urls import path
from .views import student_record_app, home

urlpatterns = [
    path('student_record_app/', student_record_app, name='student_record_app'),
    path('', home, name='home')
]