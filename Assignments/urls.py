from django.urls import path
from .views import *
urlpatterns = [
    path('assignments/',Assignments,name='assignments')
]