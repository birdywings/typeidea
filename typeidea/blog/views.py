# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.cache import cache
from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment
from comment.views import CommentShowMixin


class CommonMixin(object):
    def get_category_context(self):
        categories = Category.objects.filter(status=1)
        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)

        return {
            'nav_cates': nav_cates,
            'cates': cates,
        }

    def get_context_data(self, **kwargs):
        side_bars = SideBar.objects.filter(status=1)

        recently_posts = Post.objects.filter(status=1)[:10]
        recently_comments = Comment.objects.filter(status=1)[:10]
        hot_posts = Post.objects.filter(status=1).order_by('-pv')[:10]

        kwargs.update({
            'side_bars': side_bars,
            'recently_posts': recently_posts,
            'recently_comments': recently_comments,
            'hot_posts': hot_posts,
        })
        kwargs.update(self.get_category_context())
        return super(CommonMixin, self).get_context_data(**kwargs)


class BasePostsView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3


class IndexView(BasePostsView):
    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = super(IndexView, self).get_queryset()
        if query:
            return qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)


class CategoryView(BasePostsView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        posts = qs.filter(category_id=category_id)
        return posts


class TagView(BasePostsView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []
        posts = tag.post_set.all()
        return posts


class AuthorView(BasePostsView):
    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        qs = super(AuthorView, self).get_queryset()
        if author_id:
            qs = qs.filter(owner_id=author_id)
        return qs


class PostView(CommonMixin, CommentShowMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostView, self).get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        # 增加pv
        # 判断用户，增加uv

        session_id = self.request.COOKIES.get('sessionid')
        if not session_id:
            return

        pv_key = 'pv:%s:%s' % (session_id, self.request.path)
        if not cache.get(pv_key):
            self.object.increase_pv()
            cache.set(pv_key, 1, 30)

        uv_key = 'uv:%s:%s' % (session_id, self.request.path)
        if not cache.get(uv_key):
            self.object.increase_uv()
            cache.set(uv_key, 1, 60 * 60 * 24)






