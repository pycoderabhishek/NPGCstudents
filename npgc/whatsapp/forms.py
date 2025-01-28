from django import forms
from .models import Group
from department.models import Course, Department
from user.models import User

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'semester', 'course_id', 'department_id', 'added_by', 'group_link', 'group_description', 'group_type', 'wapp_qr', 'wapp_logo']
    
    # Additional custom fields if needed can be added here
    group_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter group name'}))
    semester = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter semester'}))
    course_id = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    department_id = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    added_by = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    group_link = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter group link'}))
    group_description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter group description', 'rows': 4}))
    group_type = forms.ChoiceField(choices=Group.GROUP_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))
    wapp_qr = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    wapp_logo = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
