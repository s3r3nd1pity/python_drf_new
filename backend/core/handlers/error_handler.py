from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def error_handler(exception:Exception,context:dict ):
    handlers={
        "JWTException":_jwt_validation_exception_handler,
    }

    response=exception_handler(exception,context)
    exception_class=exception.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exception, context )
    return response


def _jwt_validation_exception_handler(exception:Exception,context):
    return Response("JWTException expired or invalid", status=status.HTTP_401_UNAUTHORIZED)