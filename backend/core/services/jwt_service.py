from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import BlacklistMixin, Token
from typing import Type

from rest_framework.generics import get_object_or_404
from core.enums.action_token_enum import ActionTokenEnum
from core.exceptions.jwt_exception import JWTException

ActionTokenClassType=Type[BlacklistMixin|Token]

UserModel=get_user_model()

class ActionToken(BlacklistMixin, Token ):
    pass

class ActivateToken(ActionToken):
    token_type =ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.lifetime

class RecoveryToken(ActionToken):
    token_type =ActionTokenEnum.RECOVER.token_type
    lifetime = ActionTokenEnum.RECOVER.lifetime

class JWTService:
    @staticmethod
    def create_token(user,token_class:ActionTokenClassType):
        return  token_class.for_user(user)
    @staticmethod
    def verify_token(token,token_class:ActionTokenClassType):
        try:
           res= token_class(token)
           res.check_blacklist()
        except Exception:
            raise JWTException
        res.blacklist()
        user_id=res.payload.get("user_id")
        return get_object_or_404(UserModel, pk=user_id)