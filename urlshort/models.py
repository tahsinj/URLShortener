from django.db import models

# Create your models here.

class ShortURL(models.Model):
    original_url = models.URLField(max_length=700)
    short_url = models.CharField(max_length=50)
    time_date_created = models.DateTimeField()

    def __str__(self) -> str:
        return self.original_url
