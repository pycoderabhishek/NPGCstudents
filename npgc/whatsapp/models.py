from django.db import models
from user.models import User
import os
from django.utils.text import slugify

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
    wapp_qr = models.ImageField(upload_to='WHATAPP/wapp_qr', blank=True, null=True)
    wapp_logo = models.ImageField(upload_to='WHATAPP/wapp_logo', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Rename wapp_qr file
        if self.wapp_qr:
            self.wapp_qr.name = self.rename_file(self.wapp_qr.name, 'wapp_qr')

        # Rename wapp_logo file
        if self.wapp_logo:
            self.wapp_logo.name = self.rename_file(self.wapp_logo.name, 'wapp_logo')

        super(Group, self).save(*args, **kwargs)

    def rename_file(self, original_name, folder):
        # Extract file extension
        ext = os.path.splitext(original_name)[1]
        # Create new file name based on group_name
        new_name = f"{slugify(self.group_id)}{ext}"
        # Return the new name with the folder path
        return f"{new_name}"

    def __str__(self):
        return self.group_name
