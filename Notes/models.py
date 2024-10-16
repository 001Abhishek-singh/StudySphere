from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
class Notes(models.Model):
    # if User get deleted then notes data also get deleted
    subject = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
# this meta  class use to remove extra s from the model name
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = 'notes'

    