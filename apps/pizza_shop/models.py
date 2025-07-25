from django.db import models

from core.models import BaseClass


class PizzaShopModel(BaseClass):
    class Meta:
        db_table = 'pizza_shop'
    name = models.CharField(max_length=20)
