from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import User
# Create your views here.




def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def verify(request):
    user = User.objects.all().filter(name=request.POST['name'],pwd=request.POST['pwd'])
    if user:
        request.session['user'] = serializers.serialize('json',user)
        return render(request,'user_home.html')
    else:
        return render(request,'login_fail.html')

def sharethings(request):
	return render(request,'sharethings.html')

def things_can_be_borrowed(request):
	return render(request,'things_can_be_borrowed.html')

def register(request):
	user = User(name=request.POST['namer'],pwd=request.POST['pwdr'])
	user.save()
	return render(request,'login.html')
	
	
def modify_personalinfo(request):
	return render(request,'modify_personalinfo.html')
	
def modify(request):
	user = User(nickname=request.POST['nickname'],phone=request.POST['phone'],school=request.POST['school'],file=request.POST['file'],personal_intro=request.POST['personal_intro'])
	user.save()
	return render(request,'index.html')     