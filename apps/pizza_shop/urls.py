from django.urls import path

from apps.pizza_shop.views import PizzaShopListCreateView, PizzaShopRetrieveUpdateDestroyView, PizzaShopCreatePizzaView

urlpatterns = [
    path("", PizzaShopListCreateView.as_view()),
    path("/<int:pk>", PizzaShopRetrieveUpdateDestroyView.as_view()),
    path("/<int:pk>/pizzas", PizzaShopCreatePizzaView.as_view()),
]