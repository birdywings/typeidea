# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Category, Tag
from typeidea.custom_site import custom_site

@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass