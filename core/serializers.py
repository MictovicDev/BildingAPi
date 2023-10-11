from rest_framework import serializers,reverse
from .models import *
from authentication.serializers import UserSerializer
from authentication.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    image1 = serializers.ImageField(required=False)
    image2 = serializers.ImageField(required=False)
    class Meta:
        model = Project
        fields = ['id','url','image1','image2','title','categories','scope','skills','experience', 'duration','location','budget','description','time']

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
        fields = ['project','amount','duration','applicationletter','images','applicant','time']



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name','amount',]


   
class RecentProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = RecentProject
        fields = ['id','project']
    
    
class SupplierSerializer(serializers.ModelSerializer):
    # images = RequestImageSerializer(many=True)
    class Meta:
        model = SuppliersApplication
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        images_data = validated_data.pop('images')
        application = SuppliersApplication.objects.create(**validated_data)
        for image_data in images_data:
            SuppliersApplication.objects.create(project=application, **image_data)
        return application
    
class RequestSerializer(serializers.ModelSerializer):
    items =  ItemSerializer(many=True,required=False, read_only=True)
    image1 = serializers.ImageField(required=False)
    image2 = serializers.ImageField(required=False)
    uploaded_items = serializers.JSONField(write_only=True, required=False)
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    class Meta:
        model = Request
        fields = ['id','title','category','location','description','image1','image2','items','uploaded_items','time']
  
  
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
    
