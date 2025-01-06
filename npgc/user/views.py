from django.shortcuts import render
from .models import Teacher,Student,User
# Create your views here.
def home(request):
    teacher = Teacher.objects.first()  # Replace with specific filter logic
    if not teacher:
        return render(request, 'home/home.html', {"error": "No teacher found"})
    return render(request, 'home/home.html', {"teacher": teacher})


# About View
def about(request):
    """
    Renders the about page.
    """
    context = {
        'title': 'About Us',
        'message': 'Learn more about My Website and our mission.',
    }
    return render(request, 'home/about.html', context)

# Services View
def services(request):
    """
    Renders the services page.
    """
    context = {
        'title': 'Our Services',
        'message': 'Explore the services we offer at My Website.',
    }
    return render(request, 'home/services.html', context)

# Contact View

def contact(request):
    """
    Renders the contact page.
    """
    
    context = {
        'title': 'Contact Us',
        'message': 'Get in touch with us for any inquiries or support.',
    }
    return render(request, 'home/contact.html', context)