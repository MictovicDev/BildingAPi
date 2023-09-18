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
from . import email
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# class MyModelUpdateView(APIView):
#     serializer_class = MyModelSerializer

#     def put(self, request, pk):
#         my_model = get_object_or_404(MyModel, pk=pk)
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data)


class ContractorCreateView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = ContractorCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(role='Contractor')
            token = RefreshToken.for_user(user)
            user.token = token
            user.save()
            email.send_linkmail(user, token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
      
    def get(self, request):
        user = User.objects.filter(role="Contractor")
        serializer = ContractorCreateSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
class UsersUpdateView(APIView):
    def put(self,request,pk):
        user =  get_object_or_404(User, id=pk)
        # user = User.objects.get(id=pk)
        serializer = UsersUpdateSerializer(user,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        


class SupplierCreateView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = SupplierCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(role='Contractor')
            token = RefreshToken.for_user(user)
            user.token = token
            user.save()
            email.send_linkmail(user, token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
      
    def get(self, request):
        user = User.objects.filter(role="Contractor")
        serializer = ContractorCreateSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class WorkerCreateView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = WorkerCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(role='Contractor')
            token = RefreshToken.for_user(user)
            user.token = token
            user.save()
            token
            email.send_linkmail(user, token)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
      
    def get(self, request):
        user = User.objects.filter(role="Contractor")
        serializer = ContractorCreateSerializer(user, many=True)
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
            return redirect('token_obtain_pair')
            # return Response(data,status=status.HTTP_202_ACCEPTED)
        except:
            data = {'message': "User does not exist"}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        



        