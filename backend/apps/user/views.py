from rest_framework.generics import ListCreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from apps.user.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


