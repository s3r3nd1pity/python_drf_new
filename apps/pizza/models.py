from django.db import models

from apps.pizza_shop.models import PizzaShopModel
from core.models import BaseClass

from django.core.validators import MaxValueValidator, MinValueValidator


class DaysChoices(models.TextChoices):
    MONDAY = 'monday',
    TUESDAY = 'tuesday',
    WEDNESDAY = 'wednesday',
    THURSDAY = 'thursday',
    FRIDAY = "friday",
    SATURDAY = "saturday",
    SUNDAY = "sunday",


class PizzaModel(BaseClass):
    class Meta:
        db_table = 'pizza'

    name = models.CharField(max_length=20)
    size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    price = models.FloatField()
    day = models.CharField(max_length=9, choices=DaysChoices.choices)
    pizza_shop = models.ForeignKey(PizzaShopModel, related_name='pizzas', on_delete=models.CASCADE)
