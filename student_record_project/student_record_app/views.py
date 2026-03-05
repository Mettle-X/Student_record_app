from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Student
from .forms import studentForm
# from .forms import studentForm

# Create your views here.



# def student_record_app(request):
#   template = loader.get_template('students.html')
#   return HttpResponse(template.render())

def home(request):
    return HttpResponse('Welcome to student records')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_record_app/student_list.html', {'students': students})

# CREATE
def student_create(request):
    form = studentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_record_app/student_form.html', {'form': form})

# UPDATE
def student_update(request, pk):
    student = get_list_or_404(student, pk=pk)
    form = studentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student_record_app/student_form.html', {'form': form})

# DELETE
def student_delete(request, pk):
    student = get_list_or_404(student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student/student_confirm_delete.html', {'students': student})
