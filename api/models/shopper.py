from django.db import models


class Shopper(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
