from django.urls import path, include
from .views import RegisterApi, logout, CustomAuthToken

urlpatterns = [
    # path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterApi.as_view()),
    path('login/', CustomAuthToken.as_view()),
    path('logout/', logout),
]