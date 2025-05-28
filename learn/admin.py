# filepath: c:\Users\Asus\Desktop\beginning\learn\admin.py
from django.contrib import admin
from .models import CustomUser, Hotspot, Event

admin.site.register(CustomUser)
admin.site.register(Hotspot)
admin.site.register(Event)