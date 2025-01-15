
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.models import Teacher, Student
from .models import Group
from django.contrib import messages
from taksdata.models import Event,Assignment,Notification
# Login View
# Create your views here.
@login_required
def whatsapp_home(request):
    user = request.user.username
    groups=Group.objects.all()
    
    return render(request,'whatsapp/dashboard.html',{"groups":groups})