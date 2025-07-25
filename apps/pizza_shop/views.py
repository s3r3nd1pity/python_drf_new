from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response

from apps.pizza.serializers import PizzaSerializer
from apps.pizza_shop.models import PizzaShopModel
from apps.pizza_shop.serializers import PizzaShopSerializer


class PizzaShopListCreateView(ListCreateAPIView):
    queryset = PizzaShopModel.objects.all()
    serializer_class = PizzaShopSerializer
class PizzaShopRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PizzaShopModel.objects.all()
    serializer_class = PizzaShopSerializer


class PizzaShopCreatePizzaView(GenericAPIView):
    serializer_class = PizzaShopSerializer
    queryset = PizzaShopModel.objects.all()

    def post(self, request, *args, **kwargs):
        pizza_shop = self.get_object()
        data = request.data
        serializer = PizzaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(pizza_shop=pizza_shop)
        shop_serializer = PizzaShopSerializer(pizza_shop)
        return Response(shop_serializer.data, status=status.HTTP_201_CREATED)
