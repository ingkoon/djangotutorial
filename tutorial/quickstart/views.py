from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from djangotutorial.tutorial.quickstart.serializers import UserSerializer, GroupSerializer
# Create your views here.
# from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]