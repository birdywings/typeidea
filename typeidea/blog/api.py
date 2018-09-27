# -*- coding: utf-8 -*-
from rest_framework import serializers, viewsets
from rest_framework.generics import ListAPIView
from blog.models import Post


class PostsSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'created_time',
        )


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer


class PostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

