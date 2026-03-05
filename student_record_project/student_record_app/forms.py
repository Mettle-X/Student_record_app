# from django import forms
# from .models import student

# class studentForm(forms.ModelForm):
#     class Meta:
#         model = student
#         fields = ['surname', 'middle_name', 'age', 'Email', 'state_of_origin', 'department']

from django import forms
from .models import Student

class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'