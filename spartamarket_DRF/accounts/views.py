from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer, UserUpdateSerializer
from .models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
# from django.contrib.auth import authenticate, login, logout

class CreateView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if email and User.objects.filter(email=email).exists():
                return Response({'message': '중복된 email입니다.'}, status=status.HTTP_400_BAD_REQUEST)  
            user = serializer.save()
            password = serializer.validated_data['password']
            user.set_password(password)
            user.save()
            return Response({"message": "저장되었습니다", "userId": user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)
        
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return Response({'message': f'{username}님 안녕하세요!'}, status=status.HTTP_200_OK)
#         return Response({'message': '잘못된 접근입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserUpdateSerializer(user)
        return Response(serializer.data)        
    
class LogoutView(APIView):
    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response({'message': '성공적으로 로그아웃 되었습니다.'}, status.HTTP_200_OK)

class UpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, username):
        if request.user.username != username:
            return Response({'message': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        user = get_object_or_404(User, username=username)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            if username!=user.username and User.objects.filter(username=username).exists():
                return Response({'message': '중복된 username'}, status=status.HTTP_400_BAD_REQUEST)
            email = serializer.validated_data.get('email')
            if email!=user.email and User.objects.filter(email=email).exists():
                return Response({'message': '중복된 email'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': '저장되었습니다', "userId": user.id}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=400)

class PasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        user = request.user
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        if not user.check_password(old_password):
            return Response({'message': '예전 password와 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if new_password == old_password:
            return Response({'message': '동일한 password입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        return Response({'message': '변경되었습니다.'}, status=status.HTTP_200_OK)
    
class DeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        user = request.user
        password = request.data['password']
        if not user.check_password(password):
            return Response({'message': 'password가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

class FollowView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        if user != request.user:
            if user.followers.filter(pk=request.user.pk).exists():
                user.followers.remove(request.user)
                message = "팔로우 취소"
            else:
                user.followers.add(request.user)
                message = "팔로우"
            return Response({"message": message}, status=status.HTTP_200_OK)
        return Response({'message': '잘못된 접근입니다'}, status=status.HTTP_400_BAD_REQUEST)