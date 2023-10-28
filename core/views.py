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
import logging

# Create your views here.

logger = logging.getLogger(__name__)


class ProjectGetCreate(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser,]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','categories','location','description','url','skills']


    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

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
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(owner=self.request.user)
    
class ListItem(generics.ListAPIView):
    query_set = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(request__id=self.kwargs['pk'])
    
class ItemList(generics.ListAPIView):
    query_set = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(request__owner=self.request.owner)
    

    
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

    def get_object(self):
        project_id = self.kwargs['pk']
        print(project_id)
        self.request.session['project_id'] = project_id
        self.request.session.save()
        return super().get_object()
    
    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['pk'])
    


class BidProjectList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer

    def get_queryset(self, serializer):
        return BidForProject.objects.filter(applicant=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(applicant=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
class ListBidView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer

    

class ApplyRequestList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SuppliersApplication.objects.all()
    serializer_class = ApplyRequestSerializer

    def get_queryset(self):
        return SuppliersApplication.objects.all()
        # return SuppliersApplication.objects.filter(store__owner=self.request.user)
    
class ReviewsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        return Reviews.objects.filter(owner=self.request.user)
    

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        if serializer.is_valid():
            serializer.save(owner=self.request.user, reviewed=pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ReviewsView(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Reviews.objects.all()
#     serializer_class = ReviewsSerializer

#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         return Reviews.objects.filter(reviewde)
    




class HiredCount(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = HireCountSerialzier

    def get_queryset(self):
       project = Project.objects.filter(owner=self.request.user)
       print(project)
       return Project.objects.filter(owner=self.request.user)
         



class CreateApplicationView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SuppliersApplication.objects.all()
    serializer_class = ApplyRequestSerializer

    def get_queryset(self):
        return SuppliersApplication.objects.filter(myrequest__owner=self.request.user)


    def perform_create(self, serializer):
        items = serializer.validated_data.pop('uploaded_bids')
        user = self.request.user
        store, created = Store.objects.get_or_create(owner=user)
        pk = self.kwargs['pk']
        myrequest = get_object_or_404(Request, id=pk)
        if serializer.is_valid():
            application_check = SuppliersApplication.objects.filter(store=store, myrequest=myrequest)
            if not application_check:
                supplier_bid = serializer.save(store=store, myrequest=myrequest)
                if items:
                  for item in items:
                    item = BidItem.objects.create(amount=item['amount'], supplier_bid=supplier_bid)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            raise serializers.ValidationError({'message': 'You have already applied to supply for this request.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ContractorProjectApplications(generics.ListAPIView, generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer


    def get_queryset(self):
        # p_id = self.request.session.get('project_id')
        # print(f"its me the id{p_id}")
        # project = Project.objects.get(id=p_id)
        bid = BidForProject.objects.filter(project__owner=self.request.user)
        return bid





class GetProject(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return BidForProject.objects.filter(id=pk)


    
class UsersApplications(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer

    def get_queryset(self):
        return BidForProject.objects.filter(applicant=self.request.user)



class CreateBidView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer

    def get_queryset(self):
        return BidForProject.objects.filter(project__owner=self.request.user)

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        project = get_object_or_404(Project, id=pk)
        if serializer.is_valid():
            bid_check = BidForProject.objects.filter(applicant=self.request.user, project=project)
            if not bid_check:
                serializer.save(applicant=self.request.user, project=project)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            raise serializers.ValidationError({'message': 'You have already applied for this job.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AcceptBidView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer

 


class BidUpdateView(generics.UpdateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = BidForProject.objects.all()
    serializer_class = BidForProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    



class StoresView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





