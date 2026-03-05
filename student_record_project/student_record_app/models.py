from django.db import models

# Create your models here.
class Student(models.Model):
    surname = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    state_of_origin = models.CharField(max_length=15)
    department = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.surname} {self.middle_name} {self.department}"

class academics(models.Model):
    faculty = models.CharField(max_length=20)
    department = models.TextField(max_length=20)
    current_level = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.faculty} {self.department} {self.current_level}"

