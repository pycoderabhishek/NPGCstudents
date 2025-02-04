from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Programe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    programe = models.ForeignKey(Programe, on_delete=models.CASCADE,blank=True,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    duration = models.IntegerField(blank=True,null=True)  # Duration in years
    credits = models.IntegerField(blank=True,null=True)
    prerequisites = models.TextField(blank=True, null=True)
    syllabus_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
class Minor(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    courses = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name
class Vocational(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    courses = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name
class Major(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    courses = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name


