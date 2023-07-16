from django.urls import path, include
from rest_framework import routers

from .views import PostListApiView

# router = routers.DefaultRouter()
# router.register('posts',PostMVS)

urlpatterns = [
    path("posts/", PostListApiView.as_view()),
    # path("", include(router.urls)),
]
