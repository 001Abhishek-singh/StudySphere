from django.contrib import admin
from .models import Books
# Register your models here.
@admin.register(Books)
class ShowBook(admin.ModelAdmin):
    list_display = ['input']