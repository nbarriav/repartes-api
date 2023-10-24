from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Quote
from api.serializers import QuoteSerializer, QuoteDetailsSerializer
from django.db import transaction


class QuoteView(APIView):
    def get(self, request):
        status_param = request.query_params.get("status")
        capacity_param = (
            request.query_params.get("capacity")
            if request.query_params.get("capacity")
            else 0
        )
        if status_param:
            quotes = Quote.objects.filter(
                status=status_param, total_capacity__gte=capacity_param
            )
        else:
            quotes = Quote.objects.filter(total_capacity__gte=capacity_param)
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            # create a new quote
            with transaction.atomic():
                total_capacity = 0
                client = {"client": int(request.data.get("client"))}
                items = request.data.get("items")
                if not client or not items:
                    raise Exception("Client and items are required")
                serializer = QuoteSerializer(data=client)

                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                # create a new quote item
                for item in items:
                    item["quote"] = serializer.data.get("id")
                    total_capacity += item["total_size"]
                    item_serializer = QuoteDetailsSerializer(data=item)
                    if item_serializer.is_valid(raise_exception=True):
                        item_serializer.save()
                # update the total capacity
                quote = Quote.objects.get(id=serializer.data.get("id"))
                quote.total_capacity = total_capacity
                quote.save()
                return Response(QuoteSerializer(quote).data, status=201)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=400)
