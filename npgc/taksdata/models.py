from django.db import models
from department.models import Department,Course,Programe
from user.models import Teacher,User,Student

# Event Model
class Event(models.Model):
    EVENT_AUDIENCE_CHOICES = [
        ('students', 'Students'),
        ('teachers', 'Teachers'),
        ('administrators', 'Administrators'),
        ('all', 'All'),
    ]

    EVENT_TYPE_CHOICES = [
        ('seminar', 'Seminar'),
        ('workshop', 'Workshop'),
        ('cultural', 'Cultural'),
        ('academic', 'Academic'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    organizer = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    program  = models.ForeignKey(Programe, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    audience_type = models.CharField(max_length=50, choices=EVENT_AUDIENCE_CHOICES)
    registration_link = models.URLField(blank=True, null=True)
    poster_url = models.URLField(blank=True, null=True)
    feedback_form = models.URLField(blank=True, null=True)
    live_stream_link = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

# Assignment Model
class Assignment(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField(blank=True ,null=True)
    submission_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_marks = models.IntegerField()
    description = models.TextField()
    late_submission_policy = models.TextField()

    def __str__(self):
        return self.title

# Notification Model
class Notification(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    sent_to = models.CharField(max_length=200)  # Could be extended to a ManyToMany field for users
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField()
    sender = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    attachment_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
