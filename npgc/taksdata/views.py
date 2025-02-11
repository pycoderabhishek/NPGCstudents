# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event,Assignment
from .forms import AssignmentForm,EventForm
from user.models import Teacher,Student
from department.models import Department, Course

def filter_events(request):
    """Utility function to filter events based on request parameters."""
    events = Event.objects.all()
    department = request.GET.get('department')
    course = request.GET.get('course')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if department:
        events = events.filter(department_id=department)
    if course:
        events = events.filter(course_id=course)
    if start_date:
        events = events.filter(date__gte=start_date)
    if end_date:
        events = events.filter(date__lte=end_date)

    return events

@login_required
def event_management(request):
    """View for managing and displaying events."""
    user = request.user
    is_admin_or_teacher = user.role in ['administrator', 'teacher']

    if request.method == 'POST' and is_admin_or_teacher:
        form = EventForm(request.POST, user=user)  # Pass user to form
        if form.is_valid():
            event = form.save(commit=False)
            if user.role == 'teacher':
                event.organizer = user.teacher  # Assign logged-in teacher as organizer
                event.department = user.teacher.department  # Assign teacher's department
            event.save()
            messages.success(request, 'Event saved successfully!')
            return redirect('event_management')
        else:
            messages.error(request, 'Failed to save event. Please check the form for errors.')
    else:
        form = EventForm(user=user)  # Pass user to form

    departments = Department.objects.all()
    courses = Course.objects.all()
    if user.role == 'student':
        events = filter_events(request)
    else:
        events = filter_events(request)

    context = {
        'form': form,
        'departments': departments,
        'courses': courses,
        'events': events,
        'is_admin_or_teacher': is_admin_or_teacher,
    }
    return render(request, 'event/event_management.html', context)

@login_required
def delete_event(request, event_id):
    """View for deleting an event."""
    event = get_object_or_404(Event, id=event_id)
    if request.user.role not in ['administrator', 'teacher'] or request.user.teacher != event.organizer:
        messages.error(request, 'You do not have permission to delete this event.')
    else:
        event.delete()
        messages.success(request, 'Event deleted successfully!')
    return redirect('event_management')


@login_required
def delete_assignment(request, assignment_id):
    """View for deleting an event."""
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.user.role not in ['administrator', 'teacher'] or request.user.teacher != assignment.teacher:
        messages.error(request, 'You do not have permission to delete this assignment.')
    else:
        assignment.delete()
        messages.success(request, 'Assginment deleted successfully!')
    return redirect('assignment_management')


# ------------------------------------------------------------------------------------------------------------------------------

def filter_assignments(request):
    """Utility function to filter assignments based on request parameters."""
    assignments = Assignment.objects.all()
    department = request.GET.get('department')
    course = request.GET.get('course')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if department:
        assignments = assignments.filter(department_id=department)
    if course:
        assignments = assignments.filter(course_id=course)
    if start_date:
        assignments = assignments.filter(due_date__gte=start_date)
    if end_date:
        assignments = assignments.filter(due_date__lte=end_date)

    return assignments


@login_required
def assignment_management(request):
    """View for managing and displaying assignments."""
    user = request.user
    is_admin_or_teacher = user.role in ['administrator', 'teacher']

    # Handle form submission
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_management')
    else:
        form = AssignmentForm()

    # Filtering assignments based on user role
    if not(is_admin_or_teacher):
        profile = get_object_or_404(Student, user=user)  # Fetch Student profile

        # Fetch assignments that match student's minor, course, or vocational
        minor_assignments = Assignment.objects.filter(minor=profile.minor)
        course_assignments = Assignment.objects.filter(course=profile.course)
        vocational_assignments = Assignment.objects.filter(vocational=profile.vocational)
 # Combine the assignments (removes duplicates)
        assignments = minor_assignments | course_assignments | vocational_assignments
    elif is_admin_or_teacher:

        assignments = Assignment.objects.all()
    else:
        assignments = Assignment.objects.none()

    context = {
        'form': form,
        'assignments': assignments,
        'departments': Department.objects.all(),
        'courses': Course.objects.all(),
        'is_admin_or_teacher': is_admin_or_teacher,
    }
    return render(request, 'assignments/assignment_management.html', context)

@login_required
def delete_assignment(request, assignment_id):
    """View for deleting an assignment."""
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.user.role not in ['administrator', 'teacher'] or request.user.teacher != assignment.teacher:
        messages.error(request, 'You do not have permission to delete this assignment.')
    else:
        assignment.delete()
        messages.success(request, 'Assignment deleted successfully!')
    return redirect('assignment_management')
