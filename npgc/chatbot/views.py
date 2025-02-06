from django.shortcuts import render,redirect
from django.http import JsonResponse
from difflib import get_close_matches

from django.views.decorators.csrf import csrf_exempt
import json
# Predefined chatbot responses
RESPONSES = {
    "hello": "Hi there! How can I assist you?",
    "hi": "Hi there! How can I assist you?",
    "fees": "The fee payment process is available on the college portal. Navigate to 'Finance' and follow the instructions.",
    "schedule": "You can view your schedule in the dashboard under the 'Timetable' section.",
    "marks": "Your marks can be accessed by logging into your account and clicking on 'Results' in the navigation menu.",
    "library": "The library is open from 8 AM to 4 PM on weekdays. You can check available books on the library portal.",
    "hostel": "Hostel-related queries can be addressed at the Hostel Office.",
    "canteen": "The canteen serves food from 8 AM to 6 PM. The menu is updated daily on the canteen board.",
    "clubs": "You can join clubs by filling out the registration form available on the 'Clubs and Activities' page.",
    "exams": "Exam dates and schedules are published in the 'Examination' section of the portal.",
    "admissions": "Admissions queries can be addressed at the Admissions Office or via the 'Admissions' tab on the website.",
    "attendance": "Your attendance record is available under the 'Attendance' tab on your dashboard.",
    "transport": "College buses operate on predefined routes. You can view the bus schedule on the 'Transport' section.",
    "placements": "Placement details are available in the 'Placement Cell' section.",
    "contact": "For assistance, contact info@college.com or call the helpline +91-1234567890.",
}


# Find the best match for user query
def find_best_match(user_message):
    user_message = user_message.lower()
    matches = get_close_matches(user_message, RESPONSES.keys(), n=1, cutoff=0.8)
    return matches[0] if matches else "default"

# View for rendering chatbot page
def chatbot(request):
    return redirect( ' http://127.0.0.1:8000')

@csrf_exempt  # Allows POST requests without CSRF token
def get_response(request):
    try:
        # Ensure we handle both GET and POST requests
        if request.method == "GET":
            user_message = request.GET.get('message', '').strip()
        elif request.method == "POST":
            data = json.loads(request.body.decode("utf-8"))
            user_message = data.get('message', '').strip()
        else:
            return JsonResponse({"error": "Invalid request method"}, status=405)

        # Debugging - Print in PythonAnywhere logs
        print(f"Received message: {user_message}")

        if not user_message:
            return JsonResponse({'response': "Please enter a message."}, status=400)

        # Get the chatbot response
        response = find_best_match(user_message)

        # Debugging - Print in logs
        print(f"Sending response: {response}")

        return JsonResponse({'response': response}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)
    except Exception as e:
        print(f"Error in get_response: {e}")  # Log error in PythonAnywhere
        return JsonResponse({"error": "Internal Server Error"}, status=500)