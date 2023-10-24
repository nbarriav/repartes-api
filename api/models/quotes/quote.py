from django.db import models
from api.models.client import Client


STATUS_CHOICES = (
    ("pending", "pending"),
    ("in progress", "in progress"),
    ("picked up", "picked up"),
    ("delivered", "delivered"),
)


class Quote(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    total_capacity = models.IntegerField(default=0)
