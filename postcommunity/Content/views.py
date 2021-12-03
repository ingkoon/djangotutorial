from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Content
from .serializers import ContentzSerializer
# Create your views here.

# CBV(class base view)타입으로 뷰 정의
class ContentListAPI(APIView):
    def get(self, requset):
        queryset = Content.objects.all()
        print(queryset)
        serializer = ContentzSerializer(queryset, many = True)
        return Response(serializer.data)

class ContentAPI(APIView):
    def get(self, request):
        queryset = Content.objects.all()
        
