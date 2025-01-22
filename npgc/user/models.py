from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from department.models import Course
from department.models import Department


class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('administrator', 'Administrator'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # Resolve clashes with default User groups and permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    semester = models.IntegerField()
    year = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True,blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    minor = models.CharField(max_length=100, blank=True, null=True)
    vocational = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()
    gender = models.CharField(max_length=10)
    is_batch_holder = models.BooleanField(default=False)
    guardian_name = models.CharField(max_length=100)
    guardian_contact = models.CharField(max_length=15)
    admission_date = models.DateField()
    scholarship_status = models.CharField(max_length=50, blank=True, null=True)
    attendance_percentage = models.FloatField()

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    department_post = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200)
    date_of_joining = models.DateField()
    experience_years = models.IntegerField()
    subjects_assigned = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
