from rest_framework import serializers
from blog.models import Post, Test


class PostsSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'created_time',
        )


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = (
            'id', 'name', 'flag',
        )


class ProductSerializer(serializers.ModelSerializer):
    """
    产品列表
    """
    cover_url = serializers.SerializerMethodField()  # 主图url
    posts_url = serializers.SerializerMethodField()  # 详情图url列表

    class Meta:
        model = Test
        fields = (
            'id', 'name', 'cover_url', 'posts_url'
        )

    @staticmethod
    def get_cover_url(obj):
        return obj.prefix + obj.cover

    @staticmethod
    def get_posts_url(obj):
        posts_url = list()
        for post in obj.posts.split(','):
            posts_url.append(obj.prefix + post)
        return posts_url
