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


class UsersListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"no users in the daatabase yet"}, status=status.HTTP_404_NOT_FOUND)

        
class ContractorCreateView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # location = serializer.validated_data['location']['name'].capitalize()
            password = serializer.validated_data["password"]
            location = serializer.validated_data['location']
            updates = serializer.validated_data["updates"]
            user = serializer.save(role='Contractor')
            token = RefreshToken.for_user(user)
            user.token = token
            email.send_linkmail(user, token)
            user.set_password(password)
            if serializer["updates"] == True:
                user.updates = True
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
      
    def get(self, request):
        user = User.objects.filter(role="Contractor")
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
class UsersUpdateView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def put(self,request,pk):
        user =  get_object_or_404(User, id=pk)
        serializer = UsersUpdateSerializer(user,  data=request.data)
        if request.user.email == user.email:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('user does not match', status=status.HTTP_401_UNAUTHORIZED)
        

class SupplierCreateView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data["password"]
            user = serializer.save(role='Supplier')
            token = RefreshToken.for_user(user)
            user.token = token
            user.set_password(password)
            if serializer["updates"] == True:
                user.updates = True
            user.save()
            email.send_linkmail(user, token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
      
    def get(self, request):
        user = User.objects.filter(role="Supplier")
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class WorkerCreateView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data["password"]
            user = serializer.save(role='Worker')
            token = RefreshToken.for_user(user)
            user.token = token
            user.set_password(password)
            if serializer["updates"] == True:
                user.updates = True
            user.save()
            token
            email.send_linkmail(user, token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
      
    def get(self, request):
        user = User.objects.filter(role="Worker")
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
