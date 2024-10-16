from django.db import models

# Create your models here.
class Books(models.Model):
    input = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Books"
        verbose_name_plural = "Books"