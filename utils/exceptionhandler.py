import logging
from django.http import response
from rest_framework import exceptions
from rest_framework.views import exception_handler
from django.http import JsonResponse
from requests import ConnectionError



def custom_exception_handler(exc,ctx):
    print('e   pa')
    handelrs={
        'ValidationError':_handle_generic_error,
        'Http404':_handle_generic_error,
        'PermissionDenied':_handle_generic_error,
        'RuntimeError':_handle_generic_error,
        'DoesNotExist':_handle_generic_error
    }
    response = exception_handler(exc,ctx)
    print('e   pa')
    exception_class = exc.__class__.__name__
    
    if exception_class in handelrs:
        return handelrs[exception_class](exc,ctx,response)
        print('e   pa')
    return response
    
def _handle_generic_error(exc,ctx,response):
    print('e   pa')
    return response
