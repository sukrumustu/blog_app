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
    
     
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.author == self.request.user:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            
            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)
        
        return Response({'message': 'You are not authorized to update a post.'})

    def perform_update(self, serializer):
        serializer.save()

class PostDeleteApi(DestroyAPIView):
    
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]
    
    lookup_field = 'slug'
    
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == self.request.user:
        
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'You are not authorized to delete a post.'})
        

    def perform_destroy(self, instance):
        instance.delete()
    
    
    
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
        
    #     #!####### DELETE Product Stock ########
    #     product = Product.objects.get(id=instance.product_id)
    #     product.stock += instance.quantity
    #     product.save()
    #     #!##################################
        
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)


    
    
    
        
    
    
    

    
    
