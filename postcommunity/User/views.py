from django.shortcuts import render,redirect , get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import User
from .serializers import UserSerializer

# CBV(class base view)타입으로 뷰 정의
class UserListAPI(APIView): # 유저리스트 확인 API
    def get(self, request):
        queryset = User.objects.all()
        print(queryset)
        serializer = UserSerializer(queryset, many=True)        
        return Response(serializer.data)

class UserAPI(APIView): #유저 정보 확인 API
    # 유저 데이터를 저장하는 API
    def post(self, request):
        query = UserSerializer(data = request.data)                
        if query.is_valid():
            query.save()
            print(query)
            return Response(query.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    # 특정 포스트를 가져오는 API
    def get(self, request, nickname):
        if User.objects.get(nickname = nickname) is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:            
            query = User.objects.get(nickname = nickname)     
            print(query.id)            
            serializer = UserSerializer(query)         
            return Response(serializer.data)

    # 유저 데이터 수정 API
    def put(self, request, nickname):
        if User.objects.get(nickname = nickname) is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            query = User.objects.get(nickname = nickname)
            print(query)
            new_query = UserSerializer(query, data = request.data)
            if new_query.is_valid():
                new_query.save()
                return Response(new_query.data, status = status.HTTP_200_OK)
            else:
                return Response("invalid request",status = status.HTTP_400_BAD_REQUEST)

    # 유저 데이터 삭제 API
    def delete(self, request, nickname):
        query = User.objects.get(nickname = nickname)
        query.delete()
        print("delete user data", query)
        return Response("Delete test Ok",stauts = 200)
          
        
        
        
