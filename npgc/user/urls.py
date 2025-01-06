from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
      # About Page
    path('about/', views.about, name='about'),

    # Services Page'
    path('services/', views.services, name='services'),

    # Contact Page
    path('contact/', views.contact, name='contact'),
]
