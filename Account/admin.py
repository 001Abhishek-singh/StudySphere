from django.contrib import admin 
from .models import Profile

@admin.register(Profile)
class DisplayProfile(admin.ModelAdmin):
    list_display = ['user']