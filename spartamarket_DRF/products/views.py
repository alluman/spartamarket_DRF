from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        serializer = ProductSerializer(page, many=True)
        return Response(serializer.data, status=200)
    
class CreateView(APIView):
    permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        request.data['author'] = request.user.id
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({"message": "청 순 수 연", "productId": product.id}, status=201)
        else:
            return Response(serializer.errors, status=400)

class UpdateView(APIView):
    permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]
    def put(self, request, productId):
        product = get_object_or_404(Product, pk=productId)
        if request.user != product.author:
            return Response({"message": "큐 티 수 연"}, status=403)
        serializer = ProductSerializer(product, data=request.data)
        request.data['author'] = request.user.id
        if serializer.is_valid():
            product = serializer.save()
            return Response({"message": "청 순 수 연", "product_id": product.id}, status=200)
        else:
            return Response(serializer.errors, status=400)

class DeleteView(APIView): 
    permission_classes = [IsAuthenticated]
    def delete(self, request, productId):
        product = get_object_or_404(Product, pk=productId)
        if request.user != product.author:
            return Response({"message": "큐 티 수 연"}, status=403)
        product.delete()
        return Response({"message": "청 순 수 연"}, status=204)

class LikeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, productId):
        product = get_object_or_404(Product, pk=productId)
        if  product.like_user.filter(pk=request.user.pk).exists():
            product.like_user.remove(request.user)
            message = "좋아요 취소"
        else:
            product.like_user.add(request.user)
            message = "좋아요"
        return Response({"message": message}, status=200)
