from django import forms
from .models import Student_Info


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student_Info
        fields = ['sID', 'name', 'email', 'phone_number', 'course']