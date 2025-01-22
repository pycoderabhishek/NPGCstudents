from django.db import models
from user.models import User
from department.models import Course,Department
class Group(models.Model):
    GROUP_TYPES = [
        ('official', 'Official'),
        ('unofficial', 'Unofficial'),
    ]

    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255)
    semester = models.CharField(max_length=20)
    course_id = models.ForeignKey(Course,  on_delete=models.CASCADE)  # You can replace IntegerField with ForeignKey if there's a Course model
    department_id = models.ForeignKey(Department,  on_delete=models.CASCADE)  # Replace with ForeignKey if there's a Department model
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Tracks who added the group
    group_link = models.URLField(max_length=500, blank=True, null=True)  # Optional field for group links
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets timestamp on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates timestamp on modification
    group_description = models.TextField(blank=True, null=True)  # Optional detailed description
    group_type = models.CharField(max_length=20, choices=GROUP_TYPES, default='official')

    def __str__(self):
        return self.group_name
