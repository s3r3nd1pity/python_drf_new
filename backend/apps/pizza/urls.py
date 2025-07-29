
from django.urls import path

from apps.pizza.views import PizzaListCreateView, PizzaRetrieveUpdateDestroyView, PizzaAddPhoto

urlpatterns = [
    path("", PizzaListCreateView.as_view()),
    path("/<int:pk>", PizzaRetrieveUpdateDestroyView.as_view()),
    path("/<int:pk>/photos", PizzaAddPhoto.as_view()),
]

