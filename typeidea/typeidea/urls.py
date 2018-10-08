# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from blog.views import (
    IndexView, CategoryView, TagView, PostView, AuthorView
)
from config.views import LinkView
from comment.views import CommentView
from .autocomplete import CategoryAutocomplete, TagAutocomplete

import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from ckeditor_uploader import urls as uploader_urls

from blog.api import PostsViewSet, PostsView

import re
from django.views.static import serve
from django.conf.urls.static import static

from django.conf.urls import include

from django.conf import settings

router = routers.DefaultRouter()
router.register(r'post_view_set', PostsViewSet)


# def static(prefix, **kwargs):
#     return [
#         url(r'^%s(?P<path>.*)$' % re.escape(prefix.lstrip('/')), serve, kwargs=kwargs),
#     ]


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name='detail'),
    url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkView.as_view(), name='links'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),

    url(r'^admin/', xadmin.site.urls),

    url(r'^silk/', include('silk.urls', namespace='silk')),


    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),
    url(r'^api/', include(router.urls)),
    url(r'^post_view/', PostsView.as_view()),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
