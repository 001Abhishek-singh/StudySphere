from django.contrib import admin
from .models import Assignments
# Register your models here.
@admin.register(Assignments)
class ShowAssignments(admin.ModelAdmin):
    list_display = ['title', 'date']