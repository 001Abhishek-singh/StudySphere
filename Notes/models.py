from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    # if User get deleted then notes data also get deleted
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    date = models.DateField()
    notes = models.TextField()
# this meta  class use to remove extra s from the model name
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = 'notes'