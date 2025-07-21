from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from apps.pizza.models import PizzaModel
from apps.pizza.serializers import PizzaSerializer


def filter_pizza(query:QueryDict)->QuerySet:
    qs = PizzaModel.objects.all()
    for k,v in query.items():
        match k:
            case 'price_gt':
                qs=qs.filter(price__gt=v)
            case 'price_lt':
                qs=qs.filter(price__lt=v)
            case 'size_gt':
                qs=qs.filter(size__gt=v)
            case 'size_lt':
                qs=qs.filter(size__lt=v)
            case 'name_starts':
                qs=qs.filter(name__startswith=v)
            case 'name_ends':
                qs=qs.filter(name__endswith=v)
            case 'name_contains':
                qs=qs.filter(name__contains=v)
            case 'sort':
                fields=PizzaSerializer.Meta.fields
                allowed_fields=[*fields, *[f"-{field}" for field in fields]]
                if v not in allowed_fields:
                    raise ValidationError("Sorry, this field is not allowed")
                else:
                    qs=qs.order_by(v)
            case _:
                raise ValidationError('Invalid filter')
    return qs