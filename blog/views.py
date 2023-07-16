from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer, CommentSerializer, PostViewSerializer, LikeSerializer
from .models import Post, Comment, PostView, Like
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class PostListApiView(ListAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes=[AllowAny,]
    queryset = Post.objects.filter(status="d")

    # lookup_field = 'slug'
