# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'TypeIdea'
    site_title = 'TypeIdea后台'
    index_title = '首页'


custom_site = CustomSite(name='custom_admin')
