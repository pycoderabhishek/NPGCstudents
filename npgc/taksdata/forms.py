from django import forms
from .models import Event,Assignment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'organizer': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'audience_type': forms.Select(attrs={'class': 'form-control'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'registration_link': forms.URLInput(attrs={'class': 'form-control'}),
            'poster_url': forms.URLInput(attrs={'class': 'form-control'}),
            'feedback_form': forms.URLInput(attrs={'class': 'form-control'}),
            'live_stream_link': forms.URLInput(attrs={'class': 'form-control'}),
        }
        

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter assignment title'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 8}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'total_marks': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'submission_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter assignment details'}),
            'late_submission_policy': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter late submission policy'}),
        }

    def clean_total_marks(self):
        total_marks = self.cleaned_data.get('total_marks')
        if total_marks < 0:
            raise forms.ValidationError("Total marks cannot be negative.")
        return total_marks
    
    def clean_semester(self):
        semester = self.cleaned_data.get('semester')
        if semester and (semester < 1 or semester > 8):
            raise forms.ValidationError("Semester must be between 1 and 8.")
        return semester
        
