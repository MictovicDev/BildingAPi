from authentication.models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 

from rest_framework import serializers    

# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.

#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268

#     Updated for Django REST framework 3.
#     """

#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid

#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')

#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')

#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr

#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension

#         return extension
    

# class ImageSerializer(serializers.ModelSerializer):
#     image = Base64ImageField(
#         max_length=None, use_url=True,
#     )

#     class Meta:
#         model = User
#         fields = ('bvnimage')

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
   #   bvnimage = serializers.ImageField()
     class Meta:
        model = User
        fields = ('address','bvn','gov_id_image')
      
     def update(self,instance, validated_data):
         instance.address = validated_data['address']
         instance.bvn = validated_data['bvn']
         instance.gov_id_image = validated_data['gov_id_image']
         instance.save()
         return instance



     
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