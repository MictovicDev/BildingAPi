from authentication.models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers,response,status
from . import countries

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        field = 'location'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
      token = super().get_token(user)
      token['email'] = user.email
      token['role'] = user.role
      if user.image:
         token['image'] = user.image.url
      return token


class UsersUpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = UpdateUser
        fields = ('bvn','gov_id_image','address')
      
     def update(self,instance, validated_data):
         instance.address = validated_data['address']
         instance.bvn = validated_data['bvn']
         instance.gov_id_image = validated_data['gov_id_image']
        #  instance.hires = validated_data['hires']
         instance.save()
         return instance


class UserSerializer(serializers.ModelSerializer):
     update = UsersUpdateSerializer(read_only=True)
     password = serializers.CharField(write_only=True, required=True)
     id = serializers.UUIDField(read_only=True)
     role = serializers.CharField(read_only=True)

     class Meta:
        model = User
        fields = ('id','email','password','firstname','lastname','role','phone_number','location','update','updates')

     def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
     
     def validate_location(self, attrs):
         location = attrs.capitalize()
         country = countries.countries
         check = location in country
         if not check:
             raise serializers.ValidationError("Invalid Country please input a valid country")
         return attrs


        
        

     
     

      

   

  


