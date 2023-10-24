from django.db import models
from .quote import Quote
from enum import Enum
from enumfields import EnumField


class DeliveryStatus(Enum):
    PENDING = "pending"
    PICKED_UP = "picked up"
    DELIVERED = "delivered"


class QuoteDetailDelivery(models.Model):
    quote = models.ForeignKey("Quote", on_delete=models.CASCADE)
    status = EnumField(DeliveryStatus, default=DeliveryStatus.PENDING)
    pickup_order = models.IntegerField()

    def __str__(self):
        return self.quote.name + " " + self.delivery.name + " " + self.price
