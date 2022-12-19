from django.urls import path
from .views import ListCreateProductView, ProductDetailView, CategoryView

urlpatterns = [
    path('products/', ListCreateProductView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='customer-detail'), 
    path('categories/<int:pk>/',CategoryView.as_view()),
    path('categories/',CategoryView.as_view()),
]
