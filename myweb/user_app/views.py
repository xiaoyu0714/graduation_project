from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request,user_name=None):
    return render(request,'index.html')


def login(request):
    return render(request,'login.html')
