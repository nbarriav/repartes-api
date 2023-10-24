from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import QuoteAssignment, Quote, QuoteDetails, Shopper
from api.serializers import QuoteAssignmentSerializer, QuoteSerializer
from django.db import transaction
from api.views.utils.route_optimization import get_groups, find_path


class QuoteAssignmentView(APIView):
    def get(self, request):
        shopper = request.query_params.get("shopper")
        quote_assignments = QuoteAssignment.objects.filter(shopper=shopper)
        serializer = QuoteAssignmentSerializer(quote_assignments, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            with transaction.atomic():
                serializer = QuoteAssignmentSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    # Update the quote status
                    quote = Quote.objects.get(id=request.data["quote"])
                    quote.status = "in progress"
                    quote.save()
                    return Response(serializer.data, status=201)
                return Response(serializer.errors, status=400)
        except Exception as e:
            return Response(serializer.errors, status=400)


class RouteAssignmentView(APIView):
    def get(self, request):
        shopper_id = request.query_params.get("shopper")
        shopper = Shopper.objects.get(id=shopper_id)
        quote_assignments = QuoteAssignment.objects.filter(shopper=shopper_id)
        # get the quotes for each quote assignment and filter by the shopper and status
        quotes = list(
            Quote.objects.filter(
                id__in=[
                    quote_assignment.quote.id for quote_assignment in quote_assignments
                ],
                status="in progress",
            )
        )
        # get groups
        groups = get_groups(quotes, shopper.capacity)
        routes = []
        for group in groups:
            orders = {}
            clients = set()
            for quote in group:
                self.__format_orders(quote, orders, clients)
            clients = [
                {"id": client.id, "lat": client.lat, "long": client.long}
                for client in clients
            ]
            clients_path, path = find_path(clients, orders)
            routes.append({"clients": clients_path, "stores": path, "group": group})
        return Response({"routes": routes})

    def __format_orders(self, group, orders, clients):
        quote_id = group[0]
        quote = Quote.objects.get(id=quote_id)
        quote_details = QuoteDetails.objects.filter(quote=quote.id)
        for quote_detail in quote_details:
            client = quote.client
            clients.add(client)
            grocery = quote_detail.grocery
            product = str(quote_detail.product_id)
            quantity = quote_detail.quantity
            if grocery.name not in orders:
                orders[grocery.name] = {
                    "id": grocery.id,
                    "lat": grocery.lat,
                    "long": grocery.long,
                    "products": [{product: quantity}],
                }
                continue
            if {product: quantity} not in orders[grocery.name]["products"]:
                orders[grocery.name]["products"].append({product: quantity})
            else:
                idx = orders[grocery.name]["products"].index({product: quantity})
                orders[grocery.name]["products"][idx][product] += quantity
