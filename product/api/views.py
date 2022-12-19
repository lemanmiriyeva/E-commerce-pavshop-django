from rest_framework import generics
from product.models import Product_version, ProductCategory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import ProductListSerializer, CreateProductSerializer, DetailProductSerializer, CategorySerializer
from django.http import Http404



class ListCreateProductView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product_version.objects.all()
    serializer_class = ProductListSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateProductSerializer
        return super().get_serializer_class()
    

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CreateProductSerializer
    queryset = Product_version.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DetailProductSerializer
        else:
            return super().get_serializer_class()


class CategoryView(APIView):
    def get_object(self,pk):
        category_qs=ProductCategory.objects.filter(id=pk)
        if category_qs.exists():
            return category_qs.first()
        raise Http404
    def get(self,request,pk=None, *args, **kwargs):
        if pk:
            obj=self.get_object(pk)
            return Response(CategorySerializer(obj).data)
        all_categories=ProductCategory.objects.all()
        category_list=CategorySerializer(all_categories,many=True)

        return Response(category_list.data, )

    def post(self,request):
        print(request.data)
        category=CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data)
        return Response('ok')

    def put(self, request, pk=None, *args, **kwargs):
        if pk:
            obj = self.get_object(pk)
        story_serializer = CategorySerializer(data=request.data, instance=obj)
        if story_serializer.is_valid():
            story_serializer.save()
            return Response(CategorySerializer(obj).data)
        return Response(story_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
