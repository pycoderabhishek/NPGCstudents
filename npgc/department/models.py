from django.db import models

class Department(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    duration = models.IntegerField()  # Duration in years
    credits = models.IntegerField()
    course_type = models.CharField(max_length=50)
    prerequisites = models.TextField(blank=True, null=True)
    syllabus_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
class post(models.Model):
    name = models.CharField(max_length=200)
