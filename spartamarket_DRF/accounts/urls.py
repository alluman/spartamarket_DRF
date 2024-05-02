from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name='accounts'
urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create'),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password/', views.PasswordView.as_view(), name='password'),
    path('delete/', views.DeleteView.as_view(), name='delete'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('<str:username>/update/', views.UpdateView.as_view(), name='update'),
    path('<str:username>/follow/', views.FollowView.as_view(), name='follow'),
]
