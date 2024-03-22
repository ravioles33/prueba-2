from django.urls import path
from product import views

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]
