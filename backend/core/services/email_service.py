import os

from django.template.loader import get_template
from  django.core.mail import EmailMultiAlternatives

from configs.celery import app
from core.services.jwt_service import JWTService, ActivateToken
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class EmailService:
    @staticmethod
    @app.task
    def send_email(to:str, template_name:str, context:dict, subject:str)->None:
        temp=get_template(template_name=template_name)
        html_content = temp.render(context)
        msg = EmailMultiAlternatives(
            to=[to],
            from_email=os.environ.get("EMAIL_HOST_USER"),
            subject=subject,
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    @classmethod
    def register(cls, user):
        token=JWTService.create_token(user, ActivateToken)
        url = f"http://localhost/activate/{token}"
        cls.send_email.delay(to=user.email, template_name="register.html", context={"url": url, "name":user.profile.name}, subject="Register")
    @staticmethod
    @app.task()
    def spam():
        for user in UserModel.objects.all():
            EmailService.send_email(user.email, template_name="spam.html", context={}, subject="Spam")
