from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    lat = models.FloatField()
    long = models.FloatField()
