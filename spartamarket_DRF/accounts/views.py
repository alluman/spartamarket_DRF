from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404

class CreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "청 순 수 연", "userId": user.id}, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': f'{username}님 청순수연!'}, status=200)
        return Response({'message': '큐 티 수 연'}, status=401)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)        
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': '청 순 수 연'}, status=200)

