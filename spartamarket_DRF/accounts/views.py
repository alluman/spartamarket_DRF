from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

class CreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "회원가입 성공.", "user_id": user.id})
        else:
            return Response(serializer.errors, status=400)