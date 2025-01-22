# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
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
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = user.teacher if user.role == 'teacher' else None
            event.save()
            messages.success(request, 'Event saved successfully!')
            return redirect('event_management')
        else:
            messages.error(request, 'Failed to save event. Please check the form for errors.')
    else:
        form = EventForm()

    departments = Department.objects.all()
    courses = Course.objects.all()
    if user.role == 'student':
        events = filter_events(request)
    else:
        events = filter_events(request).filter(organizer=user.teacher)

    context = {
        'form': form,
        'departments': departments,
        'courses': courses,
        'events': events,
        'is_admin_or_teacher': is_admin_or_teacher,
    }
    return render(request, 'event/event_management.html', context)

@login_required
def edit_event(request, event_id):
    """View for editing an event."""
    event = get_object_or_404(Event, id=event_id)
    if request.user.role not in ['administrator', 'teacher'] or request.user.teacher != event.organizer:
        messages.error(request, 'You do not have permission to edit this event.')
        return redirect('event_management')

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_management')
    else:
        form = EventForm(instance=event)

    context = {'form': form, 'event': event}
    return render(request, 'event_edit.html', context)

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
