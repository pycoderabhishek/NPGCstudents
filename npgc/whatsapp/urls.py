from django.urls import path,include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('/',views.whatsapp_home,name='whatsapp_home')
]