from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCreateSerializer, UserUpdateSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404

class CreateView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if email and User.objects.filter(email=email).exists():
                return Response({'message': '큐 티 수 연 (이메일중복)'}, status=400)  
            user = serializer.save()
            password = serializer.validated_data['password']
            user.set_password(password)
            user.save()
            return Response({"message": "청 순 수 연", "userId": user.id}, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': f'{username}님 청순수연!'}, status=200)
        return Response({'message': '큐 티 수 연(잘못된접근)'}, status=401)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserUpdateSerializer(user)
        return Response(serializer.data)        
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': '청 순 수 연'}, status=200)

class UpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, username):
        if request.user.username != username:
            return Response({'message': '큐 티 수 연(권한없음)'}, status=403)
        user = get_object_or_404(User, username=username)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            if username!=user.username and User.objects.filter(username=username).exists():
                return Response({'message': '큐 티 수 연 (유저네임중복)'}, status=400)
            email = serializer.validated_data.get('email')
            if email!=user.email and User.objects.filter(email=email).exists():
                return Response({'message': '큐 티 수 연 (이메일중복)'}, status=400)
            serializer.save()
            return Response({'message': '청 순 수 연', "userId": user.id}, status=200)
        else:
            return Response(serializer.errors, status=400)

class PasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        user = request.user
        old_password = request.data['old_password']
        new_password = request.data['new_password']
        if not user.check_password(old_password):
            return Response({'message': '큐 티 수 연(기존)'}, status=400)
        if new_password == old_password:
            return Response({'message': '큐 티 수 연(일치)'}, status=400)
        user.set_password(new_password)
        user.save()
        return Response({'message': '청 순 수 연'}, status=200)
    
class DeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        user = request.user
        password = request.data['password']
        if not user.check_password(password):
            return Response({'message': '큐 티 수 연(불일치)'}, status=400)
        user.delete()
        return Response({"message": "청 순 수 연"}, status=204)

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
            return Response({"message": message}, status=200)
        return Response({'message': '잘못된 접근입니다'}, status=400)