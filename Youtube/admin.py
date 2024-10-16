from django.contrib import admin
from .models import YoutubeInput
# Register your models here.

@admin.register(YoutubeInput)
class ShowYoutube(admin.ModelAdmin):
    list_display = ['input']