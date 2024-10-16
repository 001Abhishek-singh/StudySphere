from django.db import models

# Create your models here.
class WikipediaList(models.Model):
    input = models.CharField(max_length=255)

    class Meta:
        verbose_name = "WikipediaList"
        verbose_name_plural = "WikipediaList"
