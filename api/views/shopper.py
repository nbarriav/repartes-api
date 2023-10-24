from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Shopper
from api.serializers import ShopperSerializer


class ShopperView(APIView):
    def get(self, request):
        shoppers = Shopper.objects.all()
        serializer = ShopperSerializer(shoppers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShopperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"errors": serializer.errors})
