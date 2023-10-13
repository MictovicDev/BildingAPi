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
    parser_classes = [MultiPartParser,]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

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
    def perform_create(self, serializer):
        items = serializer.validated_data.pop('uploaded_items')
        owner = self.request.user
        request =  serializer.save(owner=owner)
        if items:
            for item in items:
                item = Item.objects.create(name=item['name'], amount=item['amount'], request=request)
            


    
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



class BidProjectList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        owner = request.user.id
        project = BidForProject.objects.filter(project__owner=owner)
        serializer = BidForProjectSerializer(project, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBidView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer

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

    # def get_object(self,pk):
    #     applicant = self.request.user
    #     bid = BidForProject.objects.get(applicant=applicant)
    #     print(bid)
    #     return bid

    # def update(self, request, *args, **kwargs):
    #     pk = self.kwarks['pk']
    #     project = self.get_object(pk)
    #     print(request.data)
    #     serializer = self.get_serializer(project, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HireView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Hire.objects.all()
    serializer_class = HireSerializer

    def perform_create(self, serializer):
        print('yes')
        hirer = self.request.user
        pk = self.kwargs['pk']
        if serializer.is_valid():
            print('no')
            project_id = serializer.validated_data['project_id'] 
            try:
                hire,created = Hire.objects.get_or_create(hirer=hirer,hireree_id=pk,project_id=project_id)
                profile = Profile.objects.get(id=pk)
            except:
                raise serializers.ValidationError({"message":"This project has already been Given you cant hire more than one person or the project does not exists"})
            print(hire, created)
            if created == False:
                print('hello')  
                raise serializers.ValidationError({"message":"You have already hired this User for the Project"})
            profile.hires += 1
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
    

