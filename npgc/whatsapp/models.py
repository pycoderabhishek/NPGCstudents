from django.db import models
from user.models import User
import os
from django.utils.text import slugify

from department.models import Course,Department

def rename_image(instance, filename, folder):
    """
    Custom function to rename uploaded image.
    - instance: The instance of the model (Group).
    - filename: Original name of the uploaded file.
    - folder: Folder to store the image (e.g., 'wapp_qr', 'wapp_logo').
    """
    # Get group name or ID
    group_identifier = slugify(instance.group_name) if instance.group_name else f"group_{instance.group_id}"
    # Enforce .png extension
    new_filename = f"{group_identifier}_{folder}.png"
    # Return the new file path
    return f"WHATSAPP/{folder}/{new_filename}"

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
   # Custom upload_to function for QR and logo images
    wapp_qr = models.ImageField(upload_to=lambda instance, filename: rename_image(instance, filename, 'wapp_qr'), blank=True, null=True)
    wapp_logo = models.ImageField(upload_to=lambda instance, filename: rename_image(instance, filename, 'wapp_logo'), blank=True, null=True)

    def save(self, *args, **kwargs):
        # Rename wapp_qr file
        if self.wapp_qr:
            self.wapp_qr.name = self.rename_file(self.wapp_qr.name, 'wapp_qr')

        # Rename wapp_logo file
        if self.wapp_logo:
            self.wapp_logo.name = self.rename_file(self.wapp_logo.name, 'wapp_logo')

        super(Group, self).save(*args, **kwargs)


