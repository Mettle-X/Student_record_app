from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.



def student_record_app(request):
  template = loader.get_template('students.html')
  return HttpResponse(template.render())

# def student_record_app(request):
    # return render(request, 'template/students.html')

def home(request):
    return HttpResponse('Welcome to student records')
