from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.core import serializers

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if (
            not request.path.endswith('/login')
            and 'static' not in request.path
            and 'test' not in request.path
            and 'verify' not in request.path
            and 'register' not in request.path
            and 'admin' not in  request.path):
            if request.session.get('user',None):
                pass
            else:
                return HttpResponseRedirect('/user/login')
