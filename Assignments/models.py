from django.db import models

# # Create your models here.

class Assignments(models.Model):
    title = models.CharField(max_length=140,default='Null')
    description = models.CharField(max_length=140)
    location = models.CharField(max_length=160)
    date = models.DateField()
    introduction = models.TextField()
    content = models.TextField()
    conclusion = models.TextField()

    class Meta:
        verbose_name = "Assignments"
        verbose_name_plural = 'Assignments'