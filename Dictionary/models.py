from django.db import models

# Create your models here.
class Dictionary(models.Model):
    word = models.CharField(max_length=140)

    class Meta:
        verbose_name = "Dictionary"
        verbose_name_plural = "Dictionary" 