from django.contrib import admin
from .models import Department,Course,Programe,Minor,Major,Vocational

admin.site.register(Programe)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Major)
admin.site.register(Minor)
admin.site.register(Vocational)