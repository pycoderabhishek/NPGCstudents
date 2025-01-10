from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    duration = models.IntegerField(blank=True,null=True)  # Duration in years
    credits = models.IntegerField(blank=True,null=True)
    prerequisites = models.TextField(blank=True, null=True)
    syllabus_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name