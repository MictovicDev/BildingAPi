from rest_framework import serializers,reverse
from .models import *
from authentication.serializers import UserSerializer
from authentication.models import *





class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    url = serializers.CharField(read_only=True)
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    image1 = serializers.ImageField(required=False)
    image2 = serializers.ImageField(required=False)
    class Meta:
        model = Project
        fields = ['id','url','image1','image2','title','categories','scope','skills','experience','owner','duration','location','budget','description','time']
    

class ReviewsSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Reviews
        fields = '__all__'



class HireCountSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['num_hired']

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
        fields = ['id','project','amount','duration','applicationletter','images','applicant','time','accepted']

class ItemSerializer(serializers.ModelSerializer):
    request =  serializers.PrimaryKeyRelatedField(queryset=Request.objects.all())
    class Meta:
        model = Item
        fields = ['name','amount','request']

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

class BidItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidItem
        fields = ['amount']

class StoreSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Store
        fields = ['owner']


class ApplyRequestSerializer(serializers.ModelSerializer):
    myrequest = RequestSerializer(read_only=True)
    biditem = BidItemSerializer(many=True, required=False, read_only=True)
    uploaded_bids = serializers.JSONField(write_only=True,required=False,allow_null=True)
    letter = serializers.CharField(required=False)
    store = StoreSerializer(read_only=True)
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    class Meta:
        model = SuppliersApplication
        fields = ['id','myrequest','letter','store','image','time','uploaded_bids','biditem','accepted']



   
class RecentProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = RecentProject
        fields = ['id','project']
    

    
  
class StoreSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Store
        fields = '__all__'
    
