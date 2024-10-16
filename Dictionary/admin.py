from django.contrib import admin
from .models import Dictionary
# Register your models here.

@admin.register(Dictionary)
class ShowWords(admin.ModelAdmin):
    list_display = ['word']