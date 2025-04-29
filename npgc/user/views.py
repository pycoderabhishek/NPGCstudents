from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Teacher, Student,User
from django.contrib import messages
from taksdata.models import Event,Assignment,Notification
# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Attempt to authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Successful login, log the user in
                login(request, user)
                return redirect('home')  # Redirect to the home page or another page
            else:
                # Authentication failed, show an error message
                messages.error(request, "Invalid username or password")
                return render(request, 'login.html')  # Return to login page with message
        except Exception as e:
            # If there is any error during the process, log it and show a generic error message
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def home(request):
    notifications = Notification.objects.all()
    return render(request,'welcome/welcome_page.html',{'notifications':notifications})

@login_required
def dashboard(request):
    user = request.user
    role = user.role

    # Fetch role-specific data
    if role == 'teacher':
        profile = get_object_or_404(Teacher, user=user)
        events = Event.objects.filter(organizer=profile)
        assignments = Assignment.objects.filter(teacher=profile)

        context = {
            'protocol' :user,
            'profile': profile,
            'events' : events,
            'assignments': assignments
        }
    elif role == 'student':
        profile = get_object_or_404(Student, user=user)
        course = profile.course
        events = Event.objects.filter(course=course)
        assignments = Assignment.objects.filter(course=course)
        context = {
            'profile': profile,
            'events' : events[:8],
            'assignments': assignments
        }
    elif role =='administrator':
        return redirect('admin_dashboard')
    else:
        return redirect('login')

    return render(request, 'home/dashboard.html', context)
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# Unified Dashboard View
@login_required

# Logout View
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# Teacher Dashboard
@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.get(user=request.user)
    return render(request, 'home/home.html', {'teacher': teacher})

# Student Dashboard
@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    return render(request, 'home/home.html', {'student': student})

# Administrator Dashboard
@login_required
def admin_dashboard(request):
    # Get counts of students, teachers, events, assignments, etc.
    user = request.user
    role = user.role

    # Fetch role-specific data
    if role == 'Administrator':
        student_count = Student.objects.count()
        teacher_count = Teacher.objects.count()
        event_count = Event.objects.count()
        assignment_count = Assignment.objects.count()
        notification_count = Notification.objects.count()
        user=request.user
        # Pass these counts to the template
        return render(request, 'admin/dashboard.html', {
            'student_count': student_count,
            'teacher_count': teacher_count,
            'event_count': event_count,
            'assignment_count': assignment_count,
            'notification_count': notification_count,
            'user':user,
        })
    else:
        return redirect("login")
@login_required
def classroom(request):
    return render(request, 'Webpages/classroom.html')

# Placeholder Views for Model Management

@login_required
def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'admin/dashboard.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def manage_students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'teacherstaf/student_management.html', {'students': StudentForm})

@login_required
def manage_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'manage_teachers.html', {'teachers': teachers})


@login_required
def manage_assignments(request):
    assignments = Assignment.objects.all()
    return render(request, 'manage_assignments.html', {'assignments': assignments})

@login_required
def manage_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'manage_notifications.html', {'notifications': notifications})