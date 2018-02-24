# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import SideBar, Link
from typeidea.custom_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'status', 'created_time')


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'created_time')