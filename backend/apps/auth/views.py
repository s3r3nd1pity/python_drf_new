from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.user.serializers import UserSerializer
from core.services.jwt_service import JWTService, ActivateToken, SocketToken
from rest_framework.response import Response
from rest_framework import status


class ActivateUserView(GenericAPIView):
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        token = kwargs.get("token")
        user=JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SocketTokenView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        token=JWTService.create_token(user=self.request.user, token_class=SocketToken)
        return Response(str(token), status=status.HTTP_200_OK)

