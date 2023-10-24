from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Grocery
from api.serializers import GrocerySerializer


class GroceryView(APIView):
    def get(self, request):
        groceries = Grocery.objects.all()
        serializer = GrocerySerializer(groceries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GrocerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"errors": serializer.errors})
