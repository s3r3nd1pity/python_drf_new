from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models

from apps.user.managers import UserManager
from core.models import BaseModel


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ['id']
    email=models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'
        ordering = ('id',)
    name=models.CharField(max_length=255)
    surname=models.CharField(max_length=255)
    age=models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
