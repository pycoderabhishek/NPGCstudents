from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_management, name='event_management'),
    path('edit-event/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
]
