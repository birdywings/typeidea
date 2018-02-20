# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pprint import pprint as pp

from django.test import TestCase
from django.db import connection
from django.db.models import F,Q,Count,Sum
from django.test.utils import override_settings
from django.contrib.auth.models import User

from .models import Post,Tag,Category


# Create your tests here.

class Test(TestCase):
    @override_settings(DEBUG=True)
    def setUp(self):
        user = User.objects.create_user(username='lvlvlvlv')
        Tag.objects.bulk_create([
            Tag(name='tag_bulk_%s'%i, owner=user)
            for i in range(10)
        ])
        Category.objects.bulk_create([
            Category(name='category_bulk_%s'%i, owner=user)
            for i in range(10)
        ])
        Post.objects.bulk_create([
            Post(title='Post_bulk_%s'%i, owner=user,
                 category=Category.objects.first())
            for i in range(10)
        ])

        #pp(connection.queries)

    @override_settings(DEBUG=True)
    def test_filter(self):
        for i in range(1,10):
            if i>4 :
                j=2
            else :
                j=1
            post = Post.objects.get(id=i)
            post.tags.add(Tag.objects.get(id=j))

        '''
        posts = Post.objects.select_related('category').filter(Q(id=1) | Q(id=2))
        for post in posts:
            print(post.category_id)


       
        posts = Post.objects.prefetch_related('tags').filter(Q(id=1) | Q(id=6))
        post = posts.first()
        print(post.category.name)

        tag = Tag.objects.first()
        print(tag.post_set.first().title)

        cate = Category.objects.first()
        print(cate.post_set.all())


        #pp(connection.queries)
        '''
        tag = Tag.objects.values_list('name', flat=True)
        print(tag[0])