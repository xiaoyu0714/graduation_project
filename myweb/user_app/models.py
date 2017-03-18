from django.db import models

# Create your models here.
class User(models.Model):
    """用户类"""

    name = models.CharField(max_length=10)
    pwd = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10,null=True)
    phone = models.CharField(max_length=10,null=True)
    file = models.FileField(upload_to='./upload',null=True)  
    school = models.CharField(max_length=10,null=True)
    personal_intro = models.CharField(max_length=20,null=True)
    
  
class Object(models.Model):
	"""货物类"""
	
	
	objectname = models.CharField(max_length=10)
	objectnum = models.CharField(max_length=3)




