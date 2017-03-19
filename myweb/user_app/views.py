from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
from django.template import loader
from .models import User
from .forms import UploadFileForm

# Create your views here.

def userdata(request):
	user = serializers.deserialize("json", request.session['user'], ignorenonexistent=True).__next__().object
	context = {'user':user}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context, request))

def index(request):
	return userdata(request)

def login(request):
    return render(request,'login.html')

def verify(request):
    user = User.objects.all().filter(name=request.POST['name'],pwd=request.POST['pwd'])
    if user:
        request.session['user'] = serializers.serialize('json',user)
        return userdata(request)
    else:
        return render(request,'login_fail.html')

def sharethings(request):
	return render(request,'sharethings.html')

def person(request):
	return render(request,'person.html')

def register(request):
	user = User(name=request.POST['namer'],pwd=request.POST['pwdr'])
	user.save()
	return render(request,'login.html')

def modify_personalinfo(request):
	return render(request,'modify_personalinfo.html')

def modify(request):
	user = serializers.deserialize("json", request.session['user'], ignorenonexistent=True).__next__().object
	print(type(user))
	user.nickname = request.POST['nickname']
	user.phone = request.POST['phone']
	user.school = request.POST['school']
	# user.file= upload_file(request)
	user.personal_intro=request.POST['personal_intro']
	user.save()
	context = {'user':user}
	request.session['user'] = serializers.serialize('json',User.objects.all().filter(pk=user.pk))
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context, request))

def logout(request):
	request.session['user'] = None
	return render(request,'login.html')

def test(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST)
		if form.is_valid():
			print('Valid file.')
			return HttpResponseRedirect('/test')
	else:
		form = UploadFileForm()

	return render(request,'test.html',{'form':form})
