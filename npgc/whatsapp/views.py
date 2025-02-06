from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import Teacher, Student
from .models import Group
from .forms import GroupForm

@login_required
def whatsapp_home(request):
    user = request.user  # Get the logged-in user
    is_admin_or_teacher = user.role in ['administrator', 'teacher']
    role = user.role  # Assuming the `User` model has a `role` field
    groups = Group.objects.none()  # Default to an empty queryset

    if role == 'student':
        accesid = Student.objects.filter(user=user).first()  # Safely get the first record
        if accesid:
            groups = Group.objects.filter(course_id=accesid.course,semester=accesid.semester)

        # Divide groups into categories
            minor_groups = groups.filter(group_category="minor")
            major_groups = groups.filter(group_category="major")
            vocational_groups = groups.filter(group_category="vocational")
    elif role == 'teacher':
        accesid = Teacher.objects.filter(user=user).first()  # Safely get the first record
        if accesid:
            groups = Group.objects.filter(department_id=accesid.department)
            minor_groups = groups.filter(group_category="minor")
            major_groups = groups.filter(group_category="major")
            vocational_groups = groups.filter(group_category="vocational")

    elif role == 'Administrator':
        groups = Group.objects.all()  # Administrators can access all groups

    # Handle form submission for creating a new group
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            new_group = form.save(commit=False)
            # Optionally, set the 'added_by' field to the current user
            new_group.added_by = user
            new_group.save()
            return redirect('whatsapp_home')  # Redirect back to the same page after saving

    else:
        form = GroupForm()

    return render(request, 'whatsapp/dashboard.html', {
        'minors':minor_groups,
        'majors':major_groups,
        'vocationals':vocational_groups,
        'is_admin_or_teacher': is_admin_or_teacher,
        "form": form  # Pass the form to the template for rendering
    })
