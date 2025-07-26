from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.pizza.filter import PizzaFilter
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer


class PizzaListCreateView(ListAPIView):
    serializer_class = PizzaSerializer
    queryset = PizzaModel.objects.all()
    filterset_class = PizzaFilter
    permission_classes = [IsAuthenticated]


class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [IsAuthenticated]
