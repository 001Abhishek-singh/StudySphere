from django.urls import path
from .views import *
urlpatterns = [
    path('wikipedia/',wikipediafun,name='wikipedia')
]