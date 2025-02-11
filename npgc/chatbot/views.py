from django.shortcuts import render,redirect
from django.http import JsonResponse
from difflib import get_close_matches

from django.views.decorators.csrf import csrf_exempt
import json
# Predefined chatbot responses
RESPONSES = {
    "what can you do": "I can help you with fee payments, class schedules, marks, library services, hostel queries, and much more! Feel free to ask any questions, and I'll guide you.",
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hi there! How can I assist you today?",
    "fees": "You can find the fee payment process on your college portal. Please log in and navigate to the 'Finance' section for details.",
    "schedule": "Your class schedule can be viewed in the 'Timetable' section of your student portal. Log in to check it.",
    "marks": "To view your marks, log in to your portal and go to the 'Results' section.",
    "library": "The library operates from 8 AM to 4 PM on weekdays. For book availability, please check the library portal.",
    "hostel": "Hostel-related queries should be directed to the Hostel Office. For fees or rules, refer to the 'Hostel' section of the portal.",
    "exams": "For exam schedules and updates, check the 'Exams' section of your student portal for the latest information.",
    "attendance": "You can track your attendance by logging into the portal and going to the 'Attendance' section.",
    "results": "Your results will be posted in the 'Results' section of your portal after exams are graded.",
    "cafeteria": "The cafeteria is open from 7 AM to 7 PM on weekdays. You can check the menu and timings on the portal.",
    "sports": "For information on sports activities, visit the 'Sports' section on your portal or contact the Sports Office.",
    "events": "To stay informed about upcoming events, check the 'Events' section on your portal or the college's notice board.",
    "placements": "Placement details can be found under the 'Placements' section of your portal or by contacting the Placement Office.",
    "scholarships": "Scholarship details and application forms are available in the 'Scholarships' section on the portal.",
    "hostel rules": "Hostel rules and regulations can be found on your portal under the 'Hostel' section. Please review them for important guidelines.",
    "internships": "For internship opportunities, please visit the 'Internships' section of the portal or reach out to the Internship Office.",
    "admissions": "For admission-related queries, please refer to the 'Admissions' section on the portal or contact the Admissions Office.",
    "course registration": "Course registration information can be found in the 'Registration' section of your portal. Be sure to complete it before the deadline.",
    "faculty contact": "Faculty contact information can be found in the 'Faculty' section of your student portal or via the contact list shared by the department.",
    "transport": "For transport-related queries, including bus routes and timings, check the 'Transport' section on the portal or contact the transport office.",
    "counseling": "The Counseling Office provides support for academic and personal issues. Please visit their section on the portal for more information.",
    "workshops": "To know more about upcoming workshops, check the 'Workshops' section on your portal or visit the notice board.",
    "student clubs": "For information on student clubs and activities, visit the 'Clubs' section of your portal or contact the student office.",
    "alumni": "You can find alumni details and events in the 'Alumni' section on the portal. Keep an eye out for reunion announcements.",
    "id card": "For information on how to obtain or replace your student ID card, visit the 'Student Services' section on your portal.",
    "medical": "For medical assistance or health-related queries, please visit the 'Medical Center' section on the portal or contact the health office.",
    "accommodation": "For off-campus accommodation options, check the 'Accommodation' section of the portal or visit the student services office.",
    "events calendar": "The college event calendar can be found in the 'Events' section on your portal. Stay up-to-date on all activities!",
    "career guidance": "For career counseling or guidance, visit the 'Career Services' section on the portal or contact the Career Office.",
    "exam results revaluation": "If you're looking to request a revaluation for your exam results, visit the 'Results' section on the portal for details.",
    "course materials": "You can find course materials and resources in the 'Course Materials' section of the portal or contact your faculty.",
    "communication": "For updates on official communication, check the 'Notices' section on your portal or refer to your department's announcements.",
    "test schedules": "Test schedules are available in the 'Test Schedules' section of your portal. Be sure to check it regularly for updates.",
    "timetable change": "In case of timetable changes, updates will be posted in the 'Timetable' section of your portal.",
    "freshers": "For information related to freshers' orientation, please refer to the 'Freshers' section on your portal or the student office.",
    "feedback": "For feedback on services or events, visit the 'Feedback' section on the portal or contact the student services team.",
    "library events": "Upcoming events in the library can be found under the 'Library Events' section on your portal.",
    "deferral": "If you need to defer your semester, check the 'Deferral' section of your portal for the application process and guidelines.",
    "default": "I didn't quite catch that. Could you please rephrase your question?"
}



# Find the best match for user query
def find_best_match(user_message):
    user_message = user_message.lower()
    matches = get_close_matches(user_message, RESPONSES.keys(), n=1, cutoff=0.8)
    return matches[0] if matches else "default"

# View for rendering chatbot page
def chatbot(request):
    return render(request, 'chatbot_app/chatbot.html')

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