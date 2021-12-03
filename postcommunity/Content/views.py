from django.db.models import query
from django.shortcuts import render
from rest_framework import response

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from .models import Content
from .serializers import ContentSerializer
# Create your views here.

# CBV(class base view)타입으로 뷰 정의
class ContentListAPI(APIView):
    def get(self, requset):
        queryset = Content.objects.all()
        print(queryset)
        serializer = ContentSerializer(queryset, many = True)
        return Response(serializer.data)

class ContentAPI(APIView):
    def get(self, request, id):
        if Content.objects.get(id = id) is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            query = Content.objects.all()
            print(query.id)
            serializers = ContentSerializer(query)
            return Response(serializers.data)
    def post(self, request):
        query = ContentSerializer(data = request.data)
        if query.is_valid():
            query.save()
            print(query)
            return Response(query.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        if Content.objects.get(id = id) is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            query = Content.objects.get(id = id)
            print(query)
            new_query = ContentSerializer(query, data = request.data)
            if new_query.is_valid():
                new_query.save()
                return Response(new_query.data, status = status.HTTP_200_OK)
            else:
                return Response("invalid request", status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        if Content.objects.get(id = id) is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            query = Content.objects.get(id = id)
            query.delete()
            print('delete content', query.id)
            return Response("Delete content Ok", status = status.HTTP_200_OK)
        
            
        
        
