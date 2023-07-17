from django.urls import path, include
from rest_framework import routers

from .views import PostListApiView, PostCreateApi, PostDetailApi

# router = routers.DefaultRouter()
# router.register('posts',PostMVS)

urlpatterns = [
    path("list/", PostListApiView.as_view()),
    path("create/", PostCreateApi.as_view()),
    # path("detail/<int:pk>/", PostDetailApi.as_view()),
    path("detail/<str:slug>/", PostDetailApi.as_view()),
    # path("", include(router.urls)),
    
]
