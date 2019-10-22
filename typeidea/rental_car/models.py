from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='名字')
    password = models.CharField(max_length=50, verbose_name='密码')
    phone = models.CharField(max_length=50, verbose_name='电话')


class Store(models.Model):
    title = models.CharField(max_length=50, verbose_name='店铺名字')
    address = models.CharField(max_length=255, verbose_name='店铺地址')


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='分类名字')


class Car(models.Model):
    STATUS_ITEMS = (
        (0, '可租用'),
        (1, '已被租用'),
        (2, '待维修'),
    )
    name = models.CharField(max_length=50, verbose_name='名字')
    introduction = models.CharField(max_length=255, verbose_name='车辆介绍')
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name='状态')


class Order(models.Model):
    STATUS_ITEMS = (
        (0, '未付款'),
        (1, '已付款，未完成'),
        (2, '完结'),
        (3, '取消'),
    )
    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name='状态')
    car = models.ForeignKey('Car', verbose_name='车辆', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', verbose_name='用户', on_delete=models.DO_NOTHING)

