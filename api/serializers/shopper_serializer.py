from rest_framework import serializers
from api.models import Shopper


class ShopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopper
        fields = "__all__"
