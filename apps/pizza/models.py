from django.db import models
from django.core import validators as V

from apps.pizza.managers import PizzaManager
from core.enums.regex_enum import RegexEnum
from core.models import BaseModel

from apps.pizza_shop.models import PizzaShopModel

class DaysChoices(models.TextChoices):
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'

class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizza'
        ordering = ('-id',)

    name = models.CharField(max_length=30, validators=[V.RegexValidator(regex=RegexEnum.NAME.pattern, message=RegexEnum.NAME.msg)])
    size = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(100)])
    price = models.FloatField()
    day = models.CharField(max_length=9, choices=DaysChoices.choices)
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')

    objects = PizzaManager()