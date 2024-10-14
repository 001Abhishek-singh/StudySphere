from django.contrib import admin
from .models import Notes
# Register your models here.

@admin.register(Notes)
class ShowNotes(admin.ModelAdmin):
    list_display = ['subject','topic','date']