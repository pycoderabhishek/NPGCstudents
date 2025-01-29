from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'description', 'organizer', 'location', 'department', 'course', 'audience_type', 'event_type', 'registration_link', 'poster_url', 'feedback_form', 'live_stream_link']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only allow the organizer field to be pre-filled with the logged-in teacher
        if self.instance and self.instance.pk:
            self.fields['organizer'].initial = self.instance.organizer
