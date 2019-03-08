# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F


class Post(models.Model):
    STATUS_ITEMS = (
        (1, '上线'),
        (2, '草稿'),
        (3, '刪除'),
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    desc = models.CharField(max_length=255, verbose_name='摘要')
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField('Tag', verbose_name='标签')
    content = models.TextField(verbose_name='內容', help_text='目前仅支持markdown格式')
    html = models.TextField(verbose_name='渲染后的内容', default='', help_text='注：目前仅支持Markdown格式数据')
    is_markdown = models.BooleanField(verbose_name='使用markdown格式', default=True)
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    def increase_pv(self):
        return type(self).objects.filter(id=self.id).update(pv=F('pv') + 1)

    def increase_uv(self):
        return type(self).objects.filter(id=self.id).update(uv=F('uv') + 1)

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
                'codehilite': {
                    'use_pygments': False,
                    'css_class': 'prettyprint linenums',
                }
            }
            self.html = markdown.markdown(self.content, extensions=['codehilite', 'extra', 'toc'],
                                          extension_configs=config)
        else:
            self.html = self.content
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']


class Category(models.Model):
    STATUS_ITEMS = (
        (1, '可用'),
        (2, '刪除'),
    )
    name = models.CharField(max_length=50, verbose_name='类名')
    is_nav = models.BooleanField(default=False, verbose_name='是否作为导航')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建時間')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '刪除'),
    )
    name = models.CharField(max_length=50, verbose_name='标签名')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建時間')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = '标签'


class Test(models.Model):
    name = models.CharField(max_length=50, verbose_name='name',  default='')
    flag = models.IntegerField(verbose_name='flag', default=0)
    image = models.ImageField(upload_to='image',  default='')
    file = models.FileField(upload_to='file',  default='')
    num = models.CharField(max_length=50, verbose_name='num',  default='')


class Contact(models.Model):
    name = models.CharField(max_length=64, verbose_name='姓名',  default='')
    phone = models.CharField(max_length=64, verbose_name='电话',  default='')
    email = models.EmailField(max_length=64, verbose_name='邮箱', default='')
    position = models.CharField(max_length=64, verbose_name='工作岗位',  default='')
    company = models.CharField(max_length=64, verbose_name='企业名称',  default='')
    address = models.CharField(max_length=64, verbose_name='企业地址',  default='')
