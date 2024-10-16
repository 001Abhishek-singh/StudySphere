from django.urls import path,include
from .views import *
urlpatterns = [
    path('notes/',addNotes,name='notes'),
    path("updateNotes/<int:Notes_Id>",updateNotes, name='updateNotes'),
    path("deleteNotes/<int:Notes_Id>",deleteNotes,name='deleteNotes'),
]
