from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.template import loader

from .models import User,Object,Order
from .forms import UploadFileForm,UserForm
from .utils import handle_uploaded_file

from .notify_const import order_info,object_info
# Create your views here.

def get_session_user(request):
	return serializers.deserialize("json", request.session['user'], ignorenonexistent=True).__next__().object

def user_to_json(user):
	return serializers.serialize('json',user)

def index(request):
	return render(request,'index.html')

def login(request):
	if request.session.get('user',None):
		return index(request)
	return render(request,'login.html')

def verify(request):
	user = User.objects.all().filter(name=request.POST['name'],pwd=request.POST['pwd'])
	if user:
		request.session['user'] = user_to_json(user)
		return HttpResponse('login=1')
	else:
		return HttpResponse('login=0')

def register(request):
	user = User(name=request.POST['namer'],pwd=request.POST['pwdr'])
	user.save()
	return render(request,'login.html')

def logout(request):
	request.session['user'] = None
	return render(request,'login.html')

def object_upload(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			obj = Object(name=form.cleaned_data['obj_name'],
						 description=form.cleaned_data['desc'],
						 num=form.cleaned_data['obj_num'],
						 img=request.FILES['file'],
						 user=get_session_user(request))
			obj.save()
			return HttpResponse('物品添加成功！')
		else:
			return HttpResponse("Form is not valid.")
	else:
		return render(request,'object_upload.html')

def person_info(request):
	my_share = Object.objects.all().filter(user=get_session_user(request))
	orders = Order.objects.filter(user=get_session_user(request)).exclude(status='closed')[:5]
	context = {'my_share':my_share,'orders':orders}
	context['user'] = get_session_user(request)
	return render(request,'person_info.html',context)

def person_info_modify(request):
	if request.method == 'GET':
		return render(request,'person_info_modify.html')
	user = get_session_user(request)
	form = UserForm(request.POST,request.FILES,instance=user)
	if form.is_valid():
		form.save()
	else:
		return HttpResponse(form.errors)
	user = User.objects.get(pk=user.pk)
	request.session['user'] = user_to_json(user)
	return index(request)

# 提交订单
def order_submit(request):
	if request.method == 'POST':
		# 商品 id
		obj_id = request.POST.get('id',None)
		# 借出商品数
		order_num = request.POST.get('num',None)
		if not obj_id or not order_num:
			return HttpResponse(order_info['INVALID_FORM'])
		if not order_num.isdigit() or int(order_num) == 0:
			return HttpResponse(order_info['ILLEGAL_OBJECT_NUMBER'])
		# 获取objects id,
		obj = Object.objects.get(pk=obj_id)
		if not obj:
			return HttpResponse(order_info['ILLEGAL_OBJECT_ID'])
		else:
			if obj.num < int(order_num):
				return HttpResponse(order_info['OBJECT_NUMEBR_EXCEED'])
			if obj.user == get_session_user(request):
				return HttpResponse(order_info['ILLEGAL_OPERATION'])
			else:
				obj.num -= int(order_num)
				obj.save()
				order = Order(user=get_session_user(request),num=order_num,object=obj)
				order.save()
				return HttpResponse(order_info['ORDER_SUBMIT_SUCCEED'])

def search(request):
	# 物品搜索
	return render(request,'search.html')

def order_cancel(request):
	# 取消订单
	if request.method == 'POST':
		order_id = request.POST.get('order_id',None)
		if not order_id:
			return HttpResponse(order_info['ILLEGAL_ORDER_ID'])
		order = Order.objects.get(pk=order_id)
		object = order.object
		object.num += order.num
		order.status = 'closed'
		order.save()
		object.save()
		return HttpResponse('订单已取消！')
	return HttpResponse(status=404)

def borrow_things(request):
	obj_list = Object.objects.exclude(num=0)[:5]
	context = {'user':get_session_user(request),'obj_list':obj_list}
	template = loader.get_template('borrow_things.html')
	return HttpResponse(template.render(context, request))

def object_revoke(request):
	# 取消分享物品
	if request.method == 'POST':
		id = request.POST['id']
		if not id.isdigit():
			return HttpResponse(status=404)
		else:
			obj = Object.objects.get(pk=int(id))
			if obj:
				obj.delete()
				return HttpResponse(object_info['DELETE_SUCCEED'])
			else:
				return HttpResponse(order_info['ILLEGAL_OBJECT_ID'])
	else:
		return HttpResponse(status=404)
