import os

from rest_framework.generics import ListCreateAPIView, GenericAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from rest_framework.response import Response

from rest_framework import status

from apps.user.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class SendEmailTestView(GenericAPIView):
    permission_classes = [AllowAny]
    def get(self, request):
        temp=get_template('test_email.html')
        html_content=temp.render({"name":"django"})
        msg=EmailMultiAlternatives(
            subject="Test Email",
            from_email=os.environ.get('EMAIL_HOST_USER'),
            to=["shilokrov@gmail.com"]

        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return Response("Email sended", status=status.HTTP_200_OK)

