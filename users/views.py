from django.shortcuts import render
from .serializers import RegisterSerizalizer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.
class RegisterApi(CreateAPIView):
    serializer_class = RegisterSerizalizer
    queryset = User.objects.all()
    
    def create(self, request, *args, **kwargs):      # bu fonksiyon aslında CreateAPIView'den gelen ve kullanıcıyı create (register) eden fonksiyon. Signal ile yeni bir user'ın register olmasından sonra token oluşturmuştuk (yani register sonrası hemen login olacak). Ancak oluşturduğumuz Token'ı bize geri dönmesi için bu değişikliği yapmamız lazım.
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        data = serializer.data
        data["key"] = token.key     # burada key yerine token dersek register olduğumuzda "token" = ... şeklinde döner
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    
# ----------- User Login View ----------------------

#dj-rest-auth bende çalışmıyor. O nedenle drf'in hazır view'ini (obtain_auth_token) kullanarak token ile birlikte user verisinin dönmesi için onu override ediyorum.

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email, 
            'first_name': user.first_name,
            'last_name': user.last_name,
            'password': user.password,
                  
        })



    
# ----------- User Logout Function ------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Kullanıcı Çıkış (Token Sil)
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})