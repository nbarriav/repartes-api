from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import QuoteDetails
from api.serializers import QuoteSerializer, QuoteDetailsSerializer
from django.db import transaction


class QuoteDetailsView(APIView):
    def get(self, request, pk):
        quote_details = QuoteDetails.objects.filter(quote=pk)
        serializer = QuoteDetailsSerializer(quote_details, many=True)
        return Response(serializer.data)
