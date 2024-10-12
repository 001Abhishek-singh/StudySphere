from django.urls import path
from .views import *
urlpatterns = [
    path('ToDoTask/',ToDoTask,name='todo')
]