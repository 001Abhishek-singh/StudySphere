from django.db import models

# Create your models here.
class YoutubeInput(models.Model):
    input = models.CharField(max_length=255)

    class Meta:
        verbose_name = "YoutubeInput"
        verbose_name_plural = "YoutubeInput"