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
