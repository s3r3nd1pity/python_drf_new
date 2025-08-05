from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.auth.views import ActivateUserView, SocketTokenView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path("/activate/<str:token>", ActivateUserView.as_view(), name='auth_activate'),
    path("/socket", SocketTokenView.as_view(), name='auth_socket'),
]