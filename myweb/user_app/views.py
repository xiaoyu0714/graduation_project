from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.template import loader

from .models import User,Object
from .forms import UploadFileForm

# Create your views here.

def get_session_user(request):
	return 	serializers.deserialize("json", request.session['user'], ignorenonexistent=True).__next__().object

def user_to_json(user):
	return serializers.serialize('json',user)

def userdata(request):
	context = {'user':get_session_user(request)}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context, request))

def index(request):
	return userdata(request)

def login(request):
    return render(request,'login.html')

def verify(request):
	user = User.objects.all().filter(name=request.POST['name'],pwd=request.POST['pwd'])
	if user:
		request.session['user'] = user_to_json(user)
		return HttpResponse('login=1')
	else:
		return HttpResponse('login=0')

def sharethings(request):
	return render(request,'sharethings.html')

def person(request):
	return render(request,'index_per.html')

def register(request):
	user = User(name=request.POST['namer'],pwd=request.POST['pwdr'])
	user.save()
	return render(request,'login.html')

def modify_personalinfo(request):
	return render(request,'modify_personalinfo.html')

def modify(request):
	user = get_session_user(request)
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

# def object_upload(request):
# 	"""用户新增物品"""
# 	if request.method == 'POST':
# 		form = (request,POST,request.FILES)
# 		if form.is_valid():
# 			form.save()

def test(request):
	if request.method == 'POST':

		obj = Object(name=request.POST['obj_name'],
						description=request.POST['obj_desc'],
						num=request.POST['obj_num'],
						user=get_session_user(request))
		obj.save()
		return render(request,'test.html',{'form':None})
	else:
		form = UploadFileForm()
		
	return render(request,'test.html',{'form':form})
