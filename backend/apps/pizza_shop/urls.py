from django.urls import path

from apps.pizza_shop.views import PizzaShopAddPizzaView, PizzaShopListCreateView, PizzaShopRetrieveUpdateDestroyView

urlpatterns = [
    path("", PizzaShopListCreateView.as_view()),
    path("/<int:pk>", PizzaShopRetrieveUpdateDestroyView.as_view()),
    path("/<int:pk>/pizzas", PizzaShopAddPizzaView.as_view()),
]