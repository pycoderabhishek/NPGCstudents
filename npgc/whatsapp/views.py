
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import Teacher, Student
from .models import Group
@login_required
def whatsapp_home(request):
    user = request.user  # Get the logged-in user
    role = user.role  # Assuming the `User` model has a `role` field
    groups = Group.objects.none()  # Default to an empty queryset

    if role == 'student':
        accesid = Student.objects.filter(user=user).first()  # Safely get the first record
        if accesid:
            groups = Group.objects.filter(course_id=accesid.course)

    elif role == 'teacher':
        accesid = Teacher.objects.filter(user=user).first()  # Safely get the first record
        if accesid:
            groups = Group.objects.filter(department_id=accesid.department)

    elif role == 'Administrator':
        groups = Group.objects.all()  # Administrators can access all groups

    return render(request, 'whatsapp/dashboard.html', {"groups": groups})