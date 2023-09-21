from rest_framework import serializers
from .models import *





class RequestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestImage
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Project
        fields = ['image','title','categories','skills','scope','skills','experience', 'duration','location','budget','description']
        
    
class SupplierSerializer(serializers.ModelSerializer):
    images = RequestImageSerializer(many=True)
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
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    images = RequestImageSerializer(many=True)
    items =   ItemSerializer(many=True)

    class Meta:
        model = Request
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        images_data = validated_data.pop('images')
        items = validated_data.pop('items')
        request = Request.objects.create(**validated_data)
        for image_data in images_data:
            RequestImage.objects.create(request=request, **image_data)
        for item in items:
            Item.objects.create(request=request, **items)
        return request



class BidForProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidForProject
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
    
