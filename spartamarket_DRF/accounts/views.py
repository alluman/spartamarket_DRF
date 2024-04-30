from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout


class CreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "회원가입 성공.", "user_id": user.id})
        else:
            return Response(serializer.errors, status=400)
        
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': '로그인 확인'}, status=status.HTTP_200_OK)
        return Response({'message': '잘못된 입력입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': '로그아웃 되었습니다.'}, status=status.HTTP_200_OK)