from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from .serializers import PostSerializer, CommentSerializer, PostViewSerializer, LikeSerializer
from .models import Post, Comment, PostView, Like
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class PostListApiView(ListAPIView):
    
    serializer_class = PostSerializer
    permission_classes=[AllowAny,]
    queryset = Post.objects.filter(status="p")

    
    
class PostCreateApi(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated,]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class PostDetailApi(RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated,]
    
    lookup_field = 'slug'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == self.request.user:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({'message': 'There is no available post within your search parameters.'})
    
    
    
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object_or_404()
    #     if instance.author == self.request.user:
    #         serializer = self.get_serializer(instance)
    #         return Response(serializer.data)
    #     return Response(serializer.data)
    
    
class PostUpdateApi(RetrieveUpdateAPIView):
    
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated,]
    
    lookup_field = 'slug'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == self.request.user:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({'message': 'There is no available post within your search parameters.'})
    
    def update(self, request, *args, **kwargs):
        
    
    
    

    
    
