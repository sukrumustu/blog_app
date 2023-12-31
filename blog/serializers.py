from rest_framework import serializers
from .models import Post, Comment, PostView, Like
import datetime


class CommentSerializer(serializers.ModelSerializer):
    
    # user = serializers.StringRelatedField()
    # user_id = serializers.IntegerField()
    
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField()
    class Meta:
        model = Comment
        fields = ('id', 'post', 'post_id', 'time_stamp', 'content', 'user_id', 'user')




class PostSerializer(serializers.ModelSerializer):
    # comments = serializers.StringRelatedField()
    # likes = serializers.StringRelatedField()
    # post_views = serializers.StringRelatedField()
    
    author=serializers.SerializerMethodField()
    
    comments_count= serializers.SerializerMethodField()
    likes_count= serializers.SerializerMethodField()
    post_views_count= serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'category', 'image', 'comments_count', 'likes_count', 'post_views_count', 'status', 'published_date', 'last_updated', 'slug',)
        
   
    def get_comments_count(self, obj):
        return obj.comments.count()
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_post_views_count(self, obj):
        return obj.post_views.count()
    
    def get_author(self, obj):
        return obj.author.username
    
    def get_time_hour(self, obj):
        return datetime.datetime.strftime(obj.published_date, "%H:%M")
    
    def get_time_hour(self, obj):
        return datetime.datetime.strftime(obj.last_updated, "%H:%M")
    
    
        
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
        
        
        
        
        # def get_fields(self):
        # fields = super().get_fields()
        # request = self.context.get('request')
        # if request.user and not request.user.is_staff:
        #     fields.pop('availability')
        #     fields.pop('plate_number')
            
        # return fields
    
      


        
        
