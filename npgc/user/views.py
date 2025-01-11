
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Teacher, Student

# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Debugging: Print username and password
        print(f"Username: {username}, Password: {password}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'teacher':
                return redirect('teacher_dashboard')
            elif user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'administrator':
                return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')
    return render(request, 'login.html')

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
    return render(request, 'home/home.html')
