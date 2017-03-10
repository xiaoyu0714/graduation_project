from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def index(request,user_name=None):
    return render(request,'index.html')


def login(request):
    return render(request,'login.html')

def verify(request):
    user = User.objects.all().filter(name=request.POST['name'],pwd=request.POST['pwd'])
    if user:
        return render(request,'user_home.html')
    else:
        return render(request,'login_fail.html')
