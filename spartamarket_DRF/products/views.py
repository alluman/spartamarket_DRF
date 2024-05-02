from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Hashtag, Product
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        serializer = ProductSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data.copy()
        data['author'] = request.user.id
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            product = serializer.save()
            # hashtags = serializer.validated_data.get('hashtags', [])
            # for tag_name in hashtags:
            #     tag, _ = Hashtag.objects.get_or_create(name=tag_name)
            #     product.hashtags.add(tag)           
            return Response({"message": "상품을 등록하였습니다.", "productId": product.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)

class UpdateView(APIView):
    permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]
    def put(self, request, productId):
        product = get_object_or_404(Product, pk=productId)
        if request.user != product.author:
            return Response({"message": "권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProductSerializer(product, data=request.data)
        request.data['author'] = request.user.id
        if serializer.is_valid():
            product = serializer.save()
            return Response({"message": "변경하였습니다.", "product_id": product.id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)

class DeleteView(APIView): 
    permission_classes = [IsAuthenticated]
    def delete(self, request, productId):
        product = get_object_or_404(Product, pk=productId)
        if request.user != product.author:
            return Response({"message": "권한이 없습니다."}, status=status.HTTP_401_UNAUTHORIZED)
        product.delete()
        return Response({"message": "삭제하였습니다."}, status=status.HTTP_204_NO_CONTENT)

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
        return Response({"message": message}, status=status.HTTP_200_OK)

class DetailView(APIView):
    def get(self, request, productId):
        product = get_object_or_404(Product, pk=productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)             