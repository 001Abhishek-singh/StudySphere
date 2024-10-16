from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# this model is created because we want to verify user email
class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE) # creating a unique user
    auth_token = models.CharField(max_length=150) # containing authentication token it will be randomly generated
    is_valid = models.BooleanField(default=False) # checking user is valid or not
    created_date = models.DateTimeField(auto_now_add=True) # adding the current date and time

# this meta class use to remove extra s from the model name
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
    
class UserProfile(models.Model):
    # userStudent = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=160)
    email = models.EmailField()
    password = models.IntegerField()
    confirmPassword = models.IntegerField()

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfile'