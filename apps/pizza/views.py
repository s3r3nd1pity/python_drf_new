# from django.db.models import Q, Min, Max, Count
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.request import Request
# from apps.pizza.filter import filter_pizza
# from apps.pizza.models import PizzaModel
# from apps.pizza.serializers import PizzaSerializer
#
#
# class PizzaListCreateView(APIView):
#     def get(self, request:Request, **kwargs):
#         # pizzas = PizzaModel.objects.all()#we get query set
#         # pizzas = pizzas.filter(Q(size__gt=27) | Q(name="Pepperoni")).exclude(price=14.0).order_by("price").reverse()#|-or &-and, "-price" - reversed sort
#
#         # pizzas = PizzaModel.objects.all()[0:5:2]#[from:to:step]
#
#         # pizzas = PizzaModel.objects.all().values("id", "name")#Serializer will not understand cuz its no fields
#         # pizzas = PizzaModel.objects.all().aggregate(Min('size'), Max('size'))#Serializer cannot understand
#         # pizzas=PizzaModel.objects.values("name").annotate(count=Count('name'))# Annotate each pizza with the number of pizzas having the same name
#
#         qs=filter_pizza(request.query_params)
#         serializer = PizzaSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = PizzaSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class PizzaRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs["pk"]
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = PizzaSerializer(pizza)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs["pk"]
#         try:
#             pizza = PizzaModel.objects.get(pk=pk)
#         except PizzaModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         data = self.request.data
#         serializer = PizzaSerializer(pizza, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs["pk"]
#         try:
#             PizzaModel.objects.get(pk=pk).delete()
#         except PizzaModel.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         return Response(status=status.HTTP_204_NO_CONTENT)



# from rest_framework import status
# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
#
# from apps.pizza.filter import filter_pizza
# from apps.pizza.models import PizzaModel
# from apps.pizza.serializers import PizzaSerializer
#
#
# class PizzaListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     serializer_class = PizzaSerializer
#
#     def get_queryset(self):
#         return filter_pizza(self.request.query_params)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class PizzaRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = PizzaModel.objects.all()
#     serializer_class = PizzaSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):#partial_update
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

    # def get(self, *args, **kwargs):
    #     pizza = self.get_object()
    #     serializer = PizzaSerializer(pizza)
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def put(self, *args, **kwargs):
    #     pizza = self.get_object()
    #     data = self.request.data
    #     serializer = PizzaSerializer(pizza, data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def patch(self, *args, **kwargs):
    #     pizza = self.get_object()
    #     data = self.request.data
    #     serializer = PizzaSerializer(pizza, data=data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_200_OK)
    #
    # def delete(self, *args, **kwargs):
    #     self.get_object().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


#BEST ONE


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.pizza.filter import filter_pizza
from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer


class PizzaListCreateView(ListCreateAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer

    def get_queryset(self):
        return filter_pizza(self.request.query_params)
class PizzaRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PizzaModel.objects.all()
    serializer_class = PizzaSerializer
    http_method_names = ['get', 'put', 'patch', 'delete']#we can delete one and it wont work