from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({"message": "글이 작성되었습니다.", "product.id": product.id})
        else:
            return Response(serializer.errors, status=400)
#유저의 접속여부, 현재 접속중인 유저를 작성자로 등록하는 과정이 없음

class UpdateView(APIView):
    def put(self, request, productId):
        product = get_object_or_404(Product, pk=productId)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


