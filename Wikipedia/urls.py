from django.urls import path
from .views import *
urlpatterns = [
    path('wikipedia/',Wikipedia,name='wikipedia')
]