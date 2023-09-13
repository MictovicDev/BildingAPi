from djoser.serializers import UserCreateSerializer

from rest_framework import serializers

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id','email','password', 'firstname','lastname','role','image','bvn')


class RegisterSerializer(serializers.Serializer):
    pass