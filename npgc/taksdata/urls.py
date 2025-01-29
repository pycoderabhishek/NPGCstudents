from django.urls import path
from . import views

urlpatterns = [
    path('event_manage', views.event_management, name='event_management'),

    path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('delete-assignment/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
    path('assignment_manage', views.assignment_management, name='assignment_management'),

]
