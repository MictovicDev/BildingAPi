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
      if user.image:
         token['image'] = user.image.url
      return token

class UserSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True, required=True)
     id = serializers.UUIDField(read_only=True)
     role = serializers.CharField(read_only=True)
     class Meta:
        model = User
        fields = ('id','email','password','firstname','lastname','role','phone_number','location','updates')
     def validate_location(self, attrs):
         location = attrs.capitalize()
         country = countries.countries
         check = location in country
         if not check:
             raise serializers.ValidationError("Invalid Country please input a valid country")
         return attrs
         
        
class UsersUpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ('address','bvn','gov_id_image')
      
     def update(self,instance, validated_data):
         instance.address = validated_data['address']
         instance.bvn = validated_data['bvn']
         instance.gov_id_image = validated_data['gov_id_image']
         instance.save()
         return instance
     
     

      

   

  


