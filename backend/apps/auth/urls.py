from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.auth.views import ActivateUserView, RecoverPasswordRequestView, RecoverPasswordView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path("/activate/<str:token>", ActivateUserView.as_view(), name='auth_activate'),
    path("/recover", RecoverPasswordRequestView.as_view(), name='auth_recovery_request'),
    path("/recover/<str:token>", RecoverPasswordView.as_view(), name='auth_recover_password'),
]