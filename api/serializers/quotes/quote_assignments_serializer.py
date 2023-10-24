from rest_framework import serializers
from api.models import QuoteAssignment


class QuoteAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteAssignment
        fields = "__all__"
