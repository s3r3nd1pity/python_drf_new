from django.urls import path

from apps.pizza.views import PizzaListView, PizzaRetrieveUpdateDestroyView

urlpatterns = [
    path("", PizzaListView.as_view()),
    path("/<int:pk>", PizzaRetrieveUpdateDestroyView.as_view()),
]