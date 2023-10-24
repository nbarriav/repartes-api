from django.db import models
from .quote import Quote
from api.models.grocery import Grocery


class QuoteDetails(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField()
    total_size = models.FloatField()
    keyword = models.CharField(max_length=50)
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)

    def __str__(self):
        return self.item
