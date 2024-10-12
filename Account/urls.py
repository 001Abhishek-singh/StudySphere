from django.urls import path,include
from .views import *
urlpatterns = [
    path('',loginAccount,name='loginAccount'),
    path('home/',home,name='home'),
    path('add/',include('Notes.urls')),
    path('add/',include('Assignments.urls')),
    path('add/',include('Books.urls')),
    path('add/',include('Calculator.urls')),
    path('add/',include('Conversion.urls')),
    path('add/',include('Dictionary.urls')),
    path('add/',include('Map.urls')),
    path('add/',include('ToDoTask.urls')),
    path('add/',include('Wikipedia.urls')),
    path('add/',include('Youtube.urls')),
    # path('register/',registerAccount,name='registerAccount'),
    # path('checkemail/',checkemail,name='checkmail'),
    # # path('verify/<auth_token>',verify_email,name='verify'),
    # path('error/',error,name='error'),
    # path('home/',home,name='home'),
]
