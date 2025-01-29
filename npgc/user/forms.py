from django import forms
from .models import Student,Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  # Ya jo fields tumhe chahiye unka naam do

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
