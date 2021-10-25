from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.decorators import authentication_classes, permission_classes


@authentication_classes([])
@permission_classes([])
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


@authentication_classes([])
@permission_classes([])
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']