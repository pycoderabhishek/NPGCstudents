from django.contrib import admin
from .models import Department,Course,SubType,Type

admin.site.register(SubType)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Type)
