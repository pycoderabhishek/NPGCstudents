from django.urls import path,include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('whatsapp',include('whatsapp.urls')),
    path('events',include('taksdata.urls')),
    
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('administrator/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('teacher/classroom/', views.classroom, name='classroom'),

    path('admin/manage/students', views.manage_students, name='manage_students'),
    path('admin/manage/teachers/', views.manage_teachers, name='manage_teachers'),
    # path('admin/manage/events/', views.manage_events, name='manage_events'),
    path('admin/manage/assignments/', views.manage_assignments, name='manage_assignments'),
    path('admin/manage/notifications/', views.manage_notifications, name='manage_notifications'),
                   
]
