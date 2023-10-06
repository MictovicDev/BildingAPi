from django.shortcuts import render,redirect
from rest_framework import generics,response
from rest_framework.response import Response
from authentication.models import *
from authentication.serializers import *
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status, generics,permissions
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser 
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from . import email


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UsersUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        user = self.request.user
        profile = Profile.objects.get_or_create(user=user)[0]
        print(profile)
        return profile

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        print(request.data)
        serializer = self.get_serializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MyUsersUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.AllowAny]

#     def get_object(self):
        
#         user = self.request.user
#         profile = Profile.objects.get_or_create(user=user)[0]
#         print(profile)
#         return profile

#     def update(self, request, *args, **kwargs):
#         profile = self.get_object()
#         print(request.data)
#         serializer = self.get_serializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UsersUpdateView(APIView):
#     def get(self, request):
#         try:
#             user = request.user
#             profile = Profile.objects.get_or_create(user=user)
#             print(profile[0])
#             serializer = ProfileSerializer(profile[0])
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"message":"Not found"}, status=status.HTTP_404_NOT_FOUND)
        
# class UsersUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.AllowAny]
    
#     def get_object(self):
#         user = self.request.user
#         profile = Profile.objects.get_or_create(user=user)
#         return profile

#     def update(self, request, *args, **kwargs):
#         profile = self.get_object()
#         serializer = self.get_serializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersListView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"no users in the daatabase yet"}, status=status.HTTP_404_NOT_FOUND)

        
class ContractorCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.filter(role='Contractor')

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = serializer.save(role='Contractor')
            token = RefreshToken.for_user(user)
            user.token = token
            email.send_linkmail(user, token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
          
class SupplierListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.filter(role='Supplier')

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = serializer.save(role='Supplier')
            token = RefreshToken.for_user(user)
            user.token = token
            email.send_linkmail(user, token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkerListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.filter(role='Worker')

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = serializer.save(role='Worker')
            token = RefreshToken.for_user(user)
            user.token = token
            email.send_linkmail(user, token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ActivateAccount(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request,token):
        try:
            user = User.objects.get(token=token)
            user.is_active = True
            user.save()
            data = {
                'user': user.email,
                'token': user.token
            }
            return redirect('google.com')
        except:
            data = {'message': "User does not exist"}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        

class SocialAuthentication(APIView):
    def post(self, request):
        access_token = request.data.get('access_token')
