# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import markdown
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_ITEMS = (
        (1, '上线'),
        (2, '草稿'),
        (3, '刪除'),
    )
    title = models.CharField(max_length=50, verbose_name='标题')
    desc = models.CharField(max_length=255, verbose_name='摘要')
    category = models.ForeignKey('Category', verbose_name='分类')
    tags = models.ManyToManyField('Tag', verbose_name='标签')
    content = models.TextField(verbose_name='內容', help_text='目前仅支持markdown格式')
    html = models.TextField(verbose_name='渲染后的内容', default='', help_text='注：目前仅支持Markdown格式数据')
    is_markdown = models.BooleanField(verbose_name='使用markdown格式', default=True)
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
                'codehilite': {
                    'use_pygments': False,
                    'css_class': 'prettyprint linenums',
                }
            }
            self.html = markdown.markdown(self.content, extensions=["codehilite"], extension_configs=config)

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
    owner = models.ForeignKey(User, verbose_name='作者')
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建時間')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '刪除'),
    )
    name = models.CharField(max_length=50, verbose_name='标签名')
    owner = models.ForeignKey(User, verbose_name='作者')
    status = models.IntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建時間')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'
