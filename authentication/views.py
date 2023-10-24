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
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import UserLoginSerializer
from core.models import *


@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token.key)
                return Response({'token': token.key})
            print(user)
            return Response({'message': "User logged in"}, status=status.HTTP_200_OK)
        
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UsersUpdateView(generics.RetrieveUpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
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



class EditProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EditProfileSerializer
    queryset = User.objects.all()

    def get_object(self):
        user = self.request.user
        user = User.objects.get(email=user)
        return user


class MyUsersUpdateView(generics.RetrieveUpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        pk = self.kwargs['pk']
        user = User.objects.get(id=pk)
        print(user)
        profile = Profile.objects.get_or_create(user=user)[0]
        return profile

    def update(self, request,*args, **kwargs):
        profile = self.get_object()
        print(request.data)
        serializer = self.get_serializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersListView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"no users in the database yet"}, status=status.HTTP_404_NOT_FOUND)
        
class ChangePasswordView(generics.RetrieveUpdateAPIView):
    serializer_class = PassWordSerializer
    permission_classes = [IsAuthenticated]
    queryset = ChangePassword.objects.all()

    def get_object(self):
        user = self.request.user
        return user

    def update(self,request,*args,**kwargs,):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
           oldpassword = serializer.validated_data.get('oldpassword')
           newpassword = serializer.validated_data.get('newpassword')
           if user.check_password(oldpassword):
               user.set_password(newpassword)
               user.save()
               return Response({"message": "Password Changed Successfully"},status=status.HTTP_200_OK)
           raise serializers.ValidationError({"message":f"{oldpassword} Match is not found in our database"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
class ContractorCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.filter(role='ContractorRole')

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = serializer.save(role='ContractorRole')
            proflie = Profile.objects.create(user=user)
            token = str(RefreshToken.for_user(user))
            first_name = user.firstname
            useremail = user.email
            user.token = token
            user.save()
            email.send_linkmail(first_name,useremail,token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SupplierListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.filter(role='SupplierRole')

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = serializer.save(role='SupplierRole')
            proflie = Profile.objects.create(user=user)
            store = Store.objetcs.create(owner=user)
            token = str(RefreshToken.for_user(user))
            first_name = user.firstname
            useremail = user.email
            user.token = token
            user.save()
            email.send_linkmail(first_name,useremail,token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkerListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.filter(role='WorkerRole')

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = serializer.save(role='WorkerRole')
            proflie = Profile.objects.create(user=user)
            token = str(RefreshToken.for_user(user))
            first_name = user.firstname
            useremail = user.email
            user.token = token
            user.save()
            email.send_linkmail(first_name,useremail,token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ActivateAccount(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request,token):
        try:
            user = User.objects.get(token=token)
            print(user)
            user.is_active = True
            user.save()
            data = {
                'user': user.email,
                'token': user.token
            }
            return redirect('https://bilding.vercel.app/login')
        except:
            data = {'message': "User does not exist"}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        

class SocialAuthentication(APIView):
    def post(self, request):
        access_token = request.data.get('access_token')
