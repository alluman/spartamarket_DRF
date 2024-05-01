from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password/', views.PasswordView.as_view(), name='password'),
    path('delete/', views.DeleteView.as_view(), name='delete'),
    path('<str:username>/', views.ProfileView.as_view(), name='profile'),
    path('<str:username>/update/', views.UpdateView.as_view(), name='update')
]
