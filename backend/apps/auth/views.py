from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny

from apps.auth.serializers import PasswordSerializer, EmailSerializer
from apps.user.serializers import UserSerializer
from core.services.email_service import EmailService
from core.services.jwt_service import JWTService, ActivateToken, RecoveryToken
from rest_framework.response import Response
from rest_framework import status
UserModel = get_user_model()


class ActivateUserView(GenericAPIView):
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        token = kwargs.get("token")
        user=JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RecoverPasswordRequestView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, email=serializer.data['email'])
        EmailService.recover(user)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RecoverPasswordView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user=JWTService.verify_token(kwargs.get("token"), RecoveryToken)
        user.set_password(data["password"])
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

