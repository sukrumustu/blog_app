from rest_framework import serializers
from .models import Post, Comment, PostView, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'category', 'image', 'status', 'published_date', 'last_updated',)
                  
                  


class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'time_stamp', 'content',)
        
class PostViewSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    
    class Meta:
        model=PostView
        fields = ('id', 'user', 'post', 'time_stamp',)

class LikeSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    
    class Meta:
        model=Like
        fields = ('id', 'user', 'post',)
    
      


        
        
