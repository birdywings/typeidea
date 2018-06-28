# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Post, Category, Tag
from typeidea.custom_site import custom_site
from typeidea.custom_admin import BaseOwnerAdmin
from .adminforms import PostAdminForm


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator'
    ]
    list_display_links = []

    list_filter = ['category']
    search_felds = ['title', 'category__name']

    save_on_top = True
    show_full_result_count = True

    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'created_time'

    # 编辑界面
    fields = (
        ('category', 'title'),
        ('content', 'is_markdown'),
        'desc',
        'status',
        'tags',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('custom_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
