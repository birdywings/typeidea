# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import xadmin
from .models import SideBar, Link
from typeidea.adminx import BaseOwnerAdmin


class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'status', 'created_time')


xadmin.site.register(SideBar, SideBarAdmin)


class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'created_time')


xadmin.site.register(Link, LinkAdmin)
