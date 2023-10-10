from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics,permissions
from core.models import *
from core.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
# from django.contrib.sites.models import Site
from core.images import *
# Create your views here.


class ProjectGetCreate(generics.ListCreateAPIView):
    # parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        owner = self.request.user
        owner = User.objects.first()
        project = serializer.save(owner=owner)
        RecentProject.objects.create(project=project)

class RecentProjectView(generics.ListAPIView):
    queryset = RecentProject.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecentProjectSerializer


    

class RecentProjectDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,pk):
        try:
            recentproject = RecentProject.objects.filter(project__owner=pk)
            serializer = RecentProjectSerializer(recentproject, context={'request': request},many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'User with that Id does not exists'}, status=status.HTTP_404_NOT_FOUND)
    
    

class ProjectDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,pk):
        project = get_object_or_404(Project, id=pk)
        serializer = ProjectSerializer(project, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        project =  get_object_or_404(Project,id=pk)
        serializer = ProjectSerializer(project, context={'request': request}, data=request.data)
        if request.user.email == project.owner.email:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('user does not match', status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request,pk):
        try:
            project = get_object_or_404(Project, id=pk)
        except Project.DoesNotExist:
            return Response({'message': 'Project Does not exists'})
        if request.user.email == project.owner.email:
            project.delete()
            return Response({'message': 'Project Deleted Succesfully'})
        return Response({'message': 'You cant delete a Project you dont own'})


class RequestView(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]


    
class RequestDetailView(APIView):
    # parser_classes = [MultiPartParser, FormParser]
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
    
    def delete(self, request,pk):
        try:
            d_request = get_object_or_404(Request, id=pk)
        except Request.DoesNotExist:
            return Response({'message': 'Request Does not exists'})
        if request.user.email == d_request.owner.email:
            d_request.delete()
            return Response({'message': 'Request Deleted Succesfully'})
        return Response({'message': 'You cant delete a Request you dont own'}, status=status.HTTP_401_UNAUTHORIZED)


# class Application(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request):
#         application = BidProject.obje


class BidProjectList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        owner = request.user.id
        project = BidForProject.objects.filter(project__owner=owner)
        serializer = BidForProjectSerializer(project, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateBidView(APIView):
    def post(self, request,pk):
        serializer = BidForProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.validated_data.get('project')
            bid_check = BidForProject.objects.filter(applicant=request.user, project=project)
            if not bid_check:
                serializer.save(applicant=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'message': 'You cant bid for the same project again'}, status=status.HTTP_226_IM_USED)
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
    

