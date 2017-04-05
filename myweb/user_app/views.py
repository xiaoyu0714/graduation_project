from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import User,Object
from .forms import UploadFileForm
from .utils import handle_uploaded_file
# Create your views here.

def get_session_user(request):
	return 	serializers.deserialize("json", request.session['user'], ignorenonexistent=True).__next__().object

def user_to_json(user):
	return serializers.serialize('json',user)

def userdata(request):
	obj_list = Object.objects.all()
	context = {'user':get_session_user(request),'obj_list':obj_list}
	print(context)
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

def test(request):
	if request.method == 'POST':
		# print(request.POST)
		form = UploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])

			obj = Object(name=form.cleaned_data['obj_name'],
						 description=form.cleaned_data['desc'],
						 num=form.cleaned_data['obj_num'],
						 img=request.FILES['file'],
						 user=get_session_user(request))
			obj.save()

		return render(request,'test.html')
	else:
		form = UploadFileForm()

	return render(request,'test.html',{'form':form})

@csrf_exempt
def tmp(request):
	if request.method == 'POST':
		# print(request.POST)
		form = UploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			#handle_uploaded_file(request.FILES['file'])

			obj = Object(name=form.cleaned_data['obj_name'],
						 description=form.cleaned_data['desc'],
						 num=form.cleaned_data['obj_num'],
						 img=request.FILES['file'],
						 user=get_session_user(request))
			#print(obj.img)
			obj.save()
			return userdata(request)
		else:
			return HttpResponse("Form is not valid.")
	else:
		form = UploadFileForm()
		obj_list = Object.objects.all()
		return render(request,'test.html',{'form':form,'obj_list':obj_list})

def test_for_refresh(request):
	return render(request,'object_upload.html')

def test_for_person(request):
	my_share = Object.objects.all().filter(user=get_session_user(request))
	context = {'my_share':my_share}
	return render(request,'test_for_person.html',context)

def test_for_modify(request):
	return render(request,'test_for_modify.html')

# 提交订单
def order_submit(request):
	if request.method != 'POST':
		return HttpResponse(status=404)
		print(request.POST)
		# 商品 id
		obj_id = request.POST('id',None)
		# 借出商品数
		order_num = request.POST.get('num',None)
		if not obj_id or not order_num:
			return HttpResponse(status=404)

			# 获取objects id,
			obj = Object.objects.all().filter(pk=obj_id)
			if not obj:
				return HttpResponse(status=404)
			else:
				if obj.num < int(order_num):
					return HttpResponse('所借商品数超出库存')
				else:
					obj.num -= int(order_num)
					obj.save()
					return HttpResponse('成功借出。')
# 物品搜索
def search(request):
	return render(request,'search.html')
