from authentication.models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

# class UserCreateSerializer(BaseUserRegisterationSerializer):
#     class Meta(BaseUserRegisterationSerializer.Meta):
        # fields = ('id','email','password', 'firstname','lastname','role')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
      token = super().get_token(user)
      token['email'] = user.email
      if user.image:
         token['image'] = user.image.url
      return token

class ContractorCreateSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True, required=True)
     id = serializers.UUIDField(read_only=True)
     role = serializers.CharField(read_only=True)
     class Meta:
        model = User
        fields = ('id','email','password','firstname','lastname','role','phone_number','location')

        
     def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            firstname= validated_data['firstname'],
            lastname = validated_data['lastname'],
            phone_number = validated_data['phone_number'],
            location = validated_data['location'],
            password=make_password(validated_data['password'])
        )
        user.role = 'Contractor'
        user.save()
        return user
     
class UsersUpdateSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ('address', 'bvn')

     
# class UserPutSerializer(serializers.ModelSerializer):
#      class Meta:
#         model = User
#         fields = ('address','bvn')
      

class SupplierCreateSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True, required=True)
     role = serializers.CharField(read_only=True)
     class Meta:
        model = User
        fields = ('email','password','firstname','lastname','role','phone_number')

        
     def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            firstname= validated_data['firstname'],
            lastname = validated_data['lastname'],
            location = validated_data['location'],
            phone_number = validated_data['phone_number'],
            password=make_password(validated_data['password'])
        )
        user.role = 'Supplier'
        user.save()
        return user
     

class WorkerCreateSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True, required=True)
     role = serializers.CharField(read_only=True)
     class Meta:
        model = User
        fields = ('email','password','firstname','lastname','role','phone_number','location')

        
     def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            firstname= validated_data['firstname'],
            lastname = validated_data['lastname'],
            phone_number = validated_data['phone_number'],
            location = validated_data['location'],
            password=make_password(validated_data['password'])
        )
        user.role = 'Worker'
        user.save()
        return user
   

  





    
    # def update(self, instance, validated_data):
    #     print(instance)
    #     instance.role = 'Contractor'
    #     instance.save()
    #     return instance