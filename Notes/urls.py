from django.urls import path,include
from .views import *
urlpatterns = [
    path('notes/',addnotes,name='notes'),
    path('delete_note/<int:ID>',deleteNote,name='delete'),
]
