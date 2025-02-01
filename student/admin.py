from django.contrib import admin
from .models import Student_Info

# Register your models here.
class StudentsModelAdmin(admin.ModelAdmin):
    list_display = ['sID', 'name','email', 'course']

admin.site.register(Student_Info, StudentsModelAdmin)