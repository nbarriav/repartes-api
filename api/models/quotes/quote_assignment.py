from django.db import models
from .quote import Quote
from api.models.shopper import Shopper


class QuoteAssignment(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    shopper = models.ForeignKey(Shopper, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.shopper.name + " - " + self.quote.client.name
