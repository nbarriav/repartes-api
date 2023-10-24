from rest_framework import serializers
from api.models import Grocery


class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = "__all__"
