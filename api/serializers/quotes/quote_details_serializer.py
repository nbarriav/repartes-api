from rest_framework import serializers
from api.models import QuoteDetails


class QuoteDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteDetails
        fields = "__all__"
