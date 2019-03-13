from rest_framework import serializers
from blog.models import Post, Test, Product, Company


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
    video_url = serializers.SerializerMethodField()  # 视频url

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'cover_url', 'posts_url', 'video_url'
        )

    @staticmethod
    def get_cover_url(obj):
        return obj.cover_prefix + obj.cover

    @staticmethod
    def get_posts_url(obj):
        posts_url = list()
        for post in obj.posts.split(','):
            posts_url.append(obj.posts_prefix + post)
        return posts_url

    @staticmethod
    def get_video_url(obj):
        return obj.video_prefix + obj.video


class CompanySerializer(serializers.ModelSerializer):
    """
    公司信息
    """

    class Meta:
        model = Company
        fields = (
            'id', 'name', 'contact', 'phone', 'address', 'email', 'qq',
            'website', 'introduction', 'desc', 'video_url'
        )
