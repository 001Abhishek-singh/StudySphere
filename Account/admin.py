from django.contrib import admin 
from .models import Profile, UserProfile

@admin.register(Profile)
class DisplayProfile(admin.ModelAdmin):
    list_display = ['user']

@admin.register(UserProfile)
class StudentProfile(admin.ModelAdmin):
    list_display = ['name','email']