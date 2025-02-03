from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Enter the department name")
    description = models.TextField(blank=True, null=True, help_text="Brief description of the department")

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Enter the type name")
    description = models.TextField(blank=True, null=True, help_text="Brief description of the type")

    def __str__(self):
        return self.name


class SubType(models.Model):


    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Enter the course name")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="courses")
    subtype = models.ForeignKey(SubType, on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.IntegerField(blank=True, null=True, help_text="Duration in years")
    credits = models.IntegerField(blank=True, null=True, help_text="Number of credits")
    prerequisites = models.TextField(blank=True, null=True, help_text="Prerequisites for the course")
    syllabus_link = models.URLField(blank=True, null=True, help_text="URL to the syllabus")

    def __str__(self):
        return f"{self.name} ({self.department.name}) - {self.subtype.name if self.subtype else 'General'}"

