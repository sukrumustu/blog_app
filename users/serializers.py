from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password  

from dj_rest_auth.serializers import TokenSerializer

class RegisterSerizalizer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        ) 
    
    password = serializers.CharField(
        write_only=True,        
        required =True,
        validators=[validate_password],
        style ={"input_type":"password"}
        )
    
    password2 = serializers.CharField(
        write_only=True, 
        required=True,
        style ={"input_type":"password"}
        )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']
        
        # extra_kwargs ={
        #     'password': {'write_only': True},
        #     'password2': {'write_only': True}
        # }
        
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return data     
    
    
    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


#bu ikisini kullanıcı login olduğunda yalnızca token'ı değil bunun yanısıra user.data'yı da dönsün diye ekliyorum    
#! dj-rest-auth bende çalışmadı. O nedenle onu kullanmıyorum. Aşağıdaki arkadaşları yoruma alıyorum.

# class UserTokenSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = (
#             'id', 'first_name', 'last_name', 'email', 'password')

# class CustomTokenSerializer(TokenSerializer):
    
#     user = UserTokenSerializer(read_only=True)
    
    
#     class Meta(TokenSerializer.Meta):
#         fields = ('key', 'user')
        

    
    