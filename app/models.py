from django.db import models

# Create your models here.

class Lunbo(models.Model):
    img = models.CharField(max_length=256)




class Mobile(models.Model):
    img = models.CharField(max_length=100)
    content = models.CharField(max_length=240)
    sore = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    miao = models.CharField(max_length=50)
    mark = models.CharField(max_length=20)

class Phone(models.Model):
    img = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    Price = models.CharField(max_length=20)

class User(models.Model):
    email=models.CharField(max_length=50,unique=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=256)
    token=models.CharField(max_length=256)

class Cart(models.Model):
    # 用户名
    user = models.ForeignKey(User)
    # 商品
    goods = models.ForeignKey(Mobile)

    # 商品数量
    number = models.IntegerField()

