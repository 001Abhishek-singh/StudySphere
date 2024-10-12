from django.urls import path
from .views import *
urlpatterns = [
    path('books/',Books,name='searchbooks')
]