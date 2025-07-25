from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.user.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class BlockUser(GenericAPIView):
    def get_queryset(self):
        return get_user_model().objects.all().exclude(id=self.request.user.id)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeblockUser(GenericAPIView):
    def get_queryset(self):
        return get_user_model().objects.all().exclude(id=self.request.user.id)

    def patch(self, request, *args, **kwargs):
        user=self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)


class MakeUserAdmin(GenericAPIView):
    def get_queryset(self):
        return get_user_model().objects.all().exclude(id=self.request.user.id)
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
class MakeUserNotAdmin(GenericAPIView):
    def get_queryset(self):
        return get_user_model().objects.all().exclude(id=self.request.user.id)
    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

