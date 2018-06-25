from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16,default = 'Daoun')
    password = models.CharField(max_length=32)
    sex = models.CharField(max_length=1)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=11,null = True)
    email = models.CharField(max_length=50)
    pic = models.CharField(max_length=100,null= True)
    # 状态玛 0正常 1 禁用
    status = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add = True)


class Types(models.Model):
    # 无限分类
    name = models.CharField(max_length=50)
    pid = models.IntegerField()
    path = models.CharField(max_length=50)

