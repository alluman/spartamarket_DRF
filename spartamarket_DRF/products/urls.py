from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path("", views.ProductList.as_view(), name="list"),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:productId>/', views.UpdateView.as_view(), name='update'),
    path('<int:productId>/delete/', views.DeleteView.as_view(), name='delete'),
]