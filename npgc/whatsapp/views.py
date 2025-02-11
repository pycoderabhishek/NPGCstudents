from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Group
from user.models import Student,Teacher,User
from .forms import GroupForm
from django.contrib import messages
from taksdata.models import Event,Assignment,Notification
# Login View
@login_required
def whatsapp_home(request):
    user = request.user  # Get the logged-in user
    role = user.role.lower()  # Convert to lowercase for consistency
    is_admin_or_teacher = role in ['administrator', 'teacher']

    groups = Group.objects.none()  # Default to an empty queryset
    minor_groups = major_groups = vocational_groups = Group.objects.none()

    if role == 'student':
        accesid = get_object_or_404(Student, user=user)
        groups = Group.objects.filter(course_id=accesid.course, semester=accesid.semester)

    elif role == 'teacher':
        accesid = get_object_or_404(Teacher, user=user)
        groups = Group.objects.filter(department_id=accesid.department)

    elif role == 'administrator':
        groups = Group.objects.all()  # Administrators can access all groups

    # Categorizing groups
    if groups.exists():
        minor_groups = groups.filter(group_category="minor")
        major_groups = groups.filter(group_category="major")
        vocational_groups = groups.filter(group_category="vocational")

    # Handle form submission for creating a new group
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            new_group = form.save(commit=False)

            if role == 'teacher':
                teacher = get_object_or_404(Teacher, user=user)
                new_group.added_by = teacher  # Assign teacher who created the group

            new_group.save()
            return redirect('whatsapp_home')

    else:
        form = GroupForm()

    return render(request, 'whatsapp/dashboard.html', {
        'minors': minor_groups,
        'majors': major_groups,
        'vocationals': vocational_groups,
        'is_admin_or_teacher': is_admin_or_teacher,
        "form": form
    })
