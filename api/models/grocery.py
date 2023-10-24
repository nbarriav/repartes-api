from django.db import models


class Grocery(models.Model):
    name = models.CharField(max_length=50)
    api_url = models.CharField(max_length=100, unique=True)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return self.name
