from django.urls import path
from .views import *
urlpatterns = [
    path('calculator/',Calculator,name='calculator')
]