from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics,permissions
from core.models import *
from core.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

# Create your views here.


class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.POST)
        print(request.data)
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.owner)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,pk):
        project = get_object_or_404(Project, id=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class RequestList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        d_request = Request.objects.all()
        serializer = RequestSerializer(d_request, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RequestDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,pk):
        d_request= get_object_or_404(Request, id=pk)
        serializer = RequestSerializer(d_request)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class BidProjectList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        project = BidForProject.objects.all()
        serializer = BidForProjectSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.POST)
        print(request.data)
        serializer = BidForProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StoreList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.POST)
        print(request.data)
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StoreDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,pk):
        store= get_object_or_404(Request, id=pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)


    
class SupplierApplicationView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        print(request.POST)
        print(request.data)
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SupplierDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,pk):
        store= get_object_or_404(SuppliersApplication, id=pk)
        serializer = SupplierSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

