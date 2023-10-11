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
    class Meta:
        model = BidForProject
        fields = ['amount','project','duration','applicationletter','images','applicant']

# class RequestImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RequestImage
#         fields = ['image']

# class ProjectImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProjectImage
#         fields = ['image']


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
    uploaded_items = serializers.JSONField(write_only=True)
    class Meta:
        model = Request
        fields = ['id','title','category','location','description','image1','image2','items','uploaded_items']
  
    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     user = request.user
    #     title = validated_data.pop('title')
    #     category = validated_data.pop('category')
    #     location = validated_data.pop('location')
    #     description = validated_data.pop('description')
    #     image1 = validated_data.pop('image1')
    #     image2 = validated_data.pop('image2')
    #     items_data = validated_data.pop('uploaded_items')
    #     request = Request.objects.create(owner=user,image1=image1,image2=image2, title=title, category=category,location=location, description=description)
    #     print(type(items_data))
    #     return request





  
    
    
    # def create(self, validated_data):
    #     bid = BidForProject.objects.create(**validated_data)
    #     print(validated_data)
    #     return 



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
    
