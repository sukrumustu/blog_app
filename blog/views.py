from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer, CommentSerializer, PostViewSerializer, LikeSerializer
from .models import Post, Comment, PostView, Like
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class PostListCreateApiView(ListCreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
