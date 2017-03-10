from django.db import models

# Create your models here.
class User(models.Model):
    """用户类"""

    name = models.CharField(max_length=10)
    pwd = models.CharField(max_length=10)
