from django.db import models
from django.forms import Form,ModelForm

# Create your models here.
class User(models.Model):

    """用户类"""
    name = models.CharField(max_length=10)
    pwd = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10,null=True)
    phone = models.CharField(max_length=10,null=True)
    head_pic = models.FileField(default='/static/img/default.png',upload_to = 'static/img/')
    school = models.CharField(max_length=10,null=True)
    personal_intro = models.CharField(max_length=20,null=True)

class Object(models.Model):

    """货物类"""
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    num = models.IntegerField()
    img = models.FileField(default='/static/img/default.png',upload_to = 'static/img/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

class Order(models.Model):

    """订单类"""
    user = models.ForeignKey(User)
    object = models.ForeignKey(Object)
    num = models.IntegerField()
    borrow_date = models.DateField(auto_now_add=True)
    # 订单状态:active、closed.
    status = models.CharField(max_length=3,default='active')
