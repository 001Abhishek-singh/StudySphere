from django.urls import path
from .views import *
urlpatterns = [
    path('weather/',CheckWeather,name='weather')
]