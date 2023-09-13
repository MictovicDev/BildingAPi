from django.shortcuts import render
from rest_framework import generics
from authentication.models import *
from authentication.serializers import *
from django.contrib.auth import get_user_model




class RegisterView(generics.GenericAPIView):


      def post(self, request):
            user = request.data