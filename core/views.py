from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics,permissions,filters
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
    parser_classes = [MultiPartParser,]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','categories','location','description','url','skills']

    def perform_create(self, serializer):
        owner = self.request.user
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

class UserProject(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    


class RequestView(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','category','location','description']
    def perform_create(self, serializer):
        items = serializer.validated_data.pop('uploaded_items')
        owner = self.request.user
        request =  serializer.save(owner=owner)
        if items:
            for item in items:
                item = Item.objects.create(name=item['name'], amount=item['amount'], request=request)
            

class UserRequest(generics.ListAPIView):
    query_set = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(owner=self.request.user)
    

    
class GetUpdateDelRequest(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Request.objects.filter(id=self.kwargs['pk'])
    

class GetUpdateDelProject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['pk'])
    


class BidProjectList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer

    def get_queryset(self):
        return BidForProject.objects.filter(applicant=self.request.user)

    def perform_create(self, serializer):
        # pk = self.kwargs['pk']
        # project = get_object_or_404(Project, id=pk)
        if serializer.is_valid():
            bid_check = BidForProject.objects.filter(applicant=self.request.user).exists()
            if not bid_check:
                serializer.save(applicant=self.request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            raise serializers.ValidationError({'message': 'You have already applied for this job.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   



class CreateBidView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer

    def get_queryset(self):
        return BidForProject.objects.filter(applicant=self.request.user)

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        project = get_object_or_404(Project, id=pk)
        if serializer.is_valid():
            bid_check = BidForProject.objects.filter(applicant=self.request.user, project=project).exists()
            if not bid_check:
                serializer.save(applicant=self.request.user, project=project)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            raise serializers.ValidationError({'message': 'You have already applied for this job.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BidUpdateView(generics.RetrieveUpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer
    permission_classes = [permissions.IsAuthenticated]




class HireView(generics.ListCreateAPIView):
    print(dir(generics))
    permission_classes = [permissions.IsAuthenticated]
    queryset = Hire.objects.all()
    serializer_class = HireSerializer

    def perform_create(self, serializer):
        hirer = self.request.user
        pk = self.kwargs['pk']
        if serializer.is_valid():
            project_id = serializer.validated_data['project_id'] 
            print(project_id)
            hired = Hire.objects.filter(hirer=hirer, hireree_id=pk,project_id=project_id).exists()
            print(hired)
            if hired:
                raise serializers.ValidationError({"message":"You have hired this user already for this project"})
            try:
                Hire.objects.create(hirer=hirer, hireree_id=pk, project_id=project_id)
                project = Project.objects.get(id=project_id)
                project.assigned = True
                project.save()
                user = User.objects.get(id=pk)
                user.hires += 1
                user.save()
            except:
                raise serializers.ValidationError({"message":"This Project has already been Closed"})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            

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
    

