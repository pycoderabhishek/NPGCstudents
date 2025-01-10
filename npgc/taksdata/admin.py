from django.contrib import admin
from .models import Assignment,Event,Notification
# Register your models here.
admin.site.register(Assignment)
admin.site.register(Event)
admin.site.register(Notification)
