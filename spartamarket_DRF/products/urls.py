from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'
urlpatterns = [
    path("", views.ProductList.as_view(), name="list"),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:productId>/', views.DetailView.as_view(), name='detail'),
    path('<int:productId>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:productId>/delete/', views.DeleteView.as_view(), name='delete'),
    path("<int:productId>/like/", views.LikeView.as_view(), name='like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)