from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ListView(APIView):
    pass

class CreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({"message": "글이 작성되었습니다.", "product.id": product.id})
        else:
            return Response(serializer.errors, status=400)
#유저의 접속여부, 현재 접속중인 유저를 작성자로 등록하는 과정이 없음

