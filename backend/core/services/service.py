import os.path
from uuid import uuid1


def upload_pizza_photo(instance, file_name:str)->str:
    ext=file_name.split('.')[-1]
    return os.path.join(instance.pizza_shop.name, f'{uuid1()}.{ext}')