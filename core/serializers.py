from rest_framework import serializers,reverse
from .models import *
from authentication.serializers import UserSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstname','hires','location']

class BidForProjectSerializer(serializers.ModelSerializer):
    applicant = ApplicationSerializer()
    class Meta:
        model = BidForProject
        fields = '__all__'

class RequestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestImage
        fields = ['image']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name','amount',]




class ProjectSerializer(serializers.ModelSerializer):
    url = serializers.CharField(read_only=True)
    time = serializers.TimeField(read_only=True, format="%I:%M %p")
    class Meta:
        model = Project
        fields = ['id','url','image','title','categories','skills','scope','skills','experience', 'duration','location','budget','description','time']

   
   
   
class RecentProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    # projects = serializers.HyperlinkedRelatedField(view_name='project-detail',read_only=True)
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
    images = RequestImageSerializer(many=True, required=False)
    items =  ItemSerializer(many=True,required=False)
    uploaded_items = serializers.JSONField(write_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
    )
    class Meta:
        model = Request
        fields = ['id','title','category','location','description','images','items','uploaded_items','uploaded_images']
  
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        title = validated_data.pop('title')
        category = validated_data.pop('category')
        location = validated_data.pop('location')
        description = validated_data.pop('description')
        items_data = validated_data.pop('uploaded_items')
        uploaded_images = validated_data.pop('uploaded_images')
        request = Request.objects.create(owner=user, title=title, category=category,location=location, description=description)
        for item in items_data:
            Item.objects.create(request=request, name=item.get('name'), amount=item.get('amount'))
        for image in uploaded_images:
            RequestImage.objects.create(request=request, image=image)
        return request

        return request





  
    
    
    # def create(self, validated_data):
    #     bid = BidForProject.objects.create(**validated_data)
    #     print(validated_data)
    #     return 



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
    
