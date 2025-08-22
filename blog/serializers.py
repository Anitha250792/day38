# blog/serializers.py
from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "author", "content", "created_at"]

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True, source="comment_set")

    class Meta:
        model = Post
        fields = ["id", "title", "slug", "author", "content", "created_at", "updated_at", "comments"]
