from django.contrib import admin
#from .models import Student, academics
from . import models
# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.academics)

class studentAdmin(admin.ModelAdmin):
    list_display = ('surname', 'middle_name', 'age', 'email', 'state_of_origin', 'department')
    search_fields = ('surname', 'middle_name', 'Email')
    list_filter = ('department')


