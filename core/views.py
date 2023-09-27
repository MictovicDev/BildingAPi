from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics,permissions
from core.models import *
from core.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.urls import reverse
# from django.contrib.sites.models import Site
from core.images import *
# Create your views here.



class ProjectView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            image = serializer.validated_data['image']
            myproject = serializer.save(owner=request.user)
            domain = 'https://bildingapi.onrender.com'
            project_url = reverse('project-detail', args=[myproject.pk])
            url = domain + project_url
            myproject.url = url
            print(project_url)
            myproject.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class ProjectDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,pk):
        project = get_object_or_404(Project, id=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        project =  get_object_or_404(Project,id=pk)
        serializer = ProjectSerializer(project,  data=request.data)
        if request.user.email == project.owner.email:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('user does not match', status=status.HTTP_401_UNAUTHORIZED)
    

class RequestView(APIView):
    parser_classes = (MultiPartParser,FormParser)
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        d_request = Request.objects.all()
        serializer = RequestSerializer(d_request, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RequestSerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class RequestView(generics.ListCreateAPIView):
#     queryset = Request.objects.all()
#     serializer_class = RequestSerializer
    
class RequestDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,pk):
        d_request= get_object_or_404(Request, id=pk)
        serializer = RequestSerializer(d_request, context={'request':request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        d_request =  get_object_or_404(Request,id=pk)
        serializer = RequestSerializer(d_request,  data=request.data)
        if request.user.email == d_request.owner.email:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('user does not match', status=status.HTTP_401_UNAUTHORIZED)

# class RequestDetailView(generics.ListCreateAPIView):
#     queryset = Request.objects.all()
#     serializer_class = RequestSerializer
    


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
    

