from django.urls import path
from .views import *
urlpatterns = [
    path('assignments/',useAssignment,name='assignments'),
    path('result/assignments/',AddAssignment,name='addassignments'),
]