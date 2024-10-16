from django.urls import path
from .views import *
urlpatterns = [
    path('dictionary/',DictionaryWord,name='dictionary')
]