from random import choices

from django.db.models import QuerySet
from django.http import QueryDict

from rest_framework.exceptions import ValidationError

from apps.pizza.models import PizzaModel, DaysChoices

from django_filters import rest_framework as filters
class PizzaFilter(filters.FilterSet):
    lt=filters.NumberFilter(field_name='price',lookup_expr='lt')
    range=filters.RangeFilter(field_name='size')#range_min=25&range_max=60
    price_in=filters.BaseInFilter(field_name='price')#price_in=30,25,600
    day=filters.ChoiceFilter(field_name='day',choices=DaysChoices.choices)
    order = filters.OrderingFilter(
        fields=(
            "id","name",("price", "price_for_url")#in params we write second one and this working as first one
        )
    )#order=name or order=-name