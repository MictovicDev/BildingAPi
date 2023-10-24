from rest_framework import serializers,reverse
from .models import *
from authentication.serializers import UserSerializer
from authentication.models import *




class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name','amount',]

class BidItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidItem
        fields = ['name','amount',]



class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    url = serializers.CharField(read_only=True)
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    image1 = serializers.ImageField(required=False)
    image2 = serializers.ImageField(required=False)
    class Meta:
        model = Project
        fields = ['id','url','image1','image2','title','categories','scope','skills','experience','owner','duration','location','budget','description','time']
    


class HireSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    project_id = serializers.IntegerField(required=False)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Hire
        fields = ['project','time','project_id']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstname','hires','location']

class BidForProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    applicant = UserSerializer(read_only=True)
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    class Meta:
        model = BidForProject
        fields = ['id','project','amount','duration','applicationletter','images','applicant','time']

class RequestSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    items =  ItemSerializer(many=True,required=False, read_only=True)
    image1 = serializers.ImageField(required=False)
    image2 = serializers.ImageField(required=False)
    uploaded_items = serializers.JSONField(write_only=True,required=False,allow_null=True)
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    class Meta:
        model = Request
        fields = ['id','title','category','location','owner','description','image1','image2','items','uploaded_items','time']


class StoreSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Store
        fields = ['owner']


class ApplyRequestSerializer(serializers.ModelSerializer):
    request = RequestSerializer(read_only=True)
    biditem = BidItemSerializer(many=True, required=False, read_only=True)
    uploaded_bids = serializers.JSONField(write_only=True,required=False,allow_null=True)
    store = StoreSerializer(read_only=True)
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    class Meta:
        model = SuppliersApplication
        fields = ['id','request','letter','store','image','time','uploaded_bids','biditem']







   
class RecentProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = RecentProject
        fields = ['id','project']
    
    
# class SupplierSerializer(serializers.ModelSerializer):
#     # images = RequestImageSerializer(many=True)
#     class Meta:
#         model = SuppliersApplication
#         fields = '__all__'

#     def create(self, validated_data):
#         print(validated_data)
#         images_data = validated_data.pop('images')
#         application = SuppliersApplication.objects.create(**validated_data)
#         for image_data in images_data:
#             SuppliersApplication.objects.create(project=application, **image_data)
#         return application
    

  
  
class StoreSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Store
        fields = '__all__'
    
