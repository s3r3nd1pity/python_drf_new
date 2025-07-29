import os

from django.template.loader import get_template
from  django.core.mail import EmailMultiAlternatives

from core.services.jwt_service import JWTService, ActionToken, ActivateToken


class EmailService:
    @classmethod
    def __send_email(cls,to:str, template_name:str, context:dict, subject:str):
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
        cls.__send_email(to=user.email, template_name="register.html", context={"url": url, "name":user.profile.name}, subject="Register")
