from rest_framework import serializers
from product.models import Product_version, Discount, Designer, Image, ProductCategory
from drf_writable_nested.serializers import WritableNestedModelSerializer


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (
            'is_percent',
            'amount',
        )


class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = (
            'id',
            'designer',
        )


class ImageSerializer(serializers.ModelSerializer): 
    img= serializers.SerializerMethodField()
    def get_img(self, obj):
        return 'http://127.0.0.1:8000'+ obj.img.url
    class Meta: 
        model = Image 
        fields = ('id', 'img', )  


class DetailProductSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer()
    designer = DesignSerializer()
    brand = serializers.CharField(source = 'product.brand')
    large_desc = serializers.CharField(source = 'product.large_desc')

    images = serializers.SerializerMethodField() 
    def get_images(self, product):
        return ImageSerializer(product.images.filter(is_main=True), many=True).data
   
    class Meta:
        model = Product_version
        fields = (
                  'title', 
                  'price',
                  'discount',
                  'images',
                  'large_desc',
                  'designer', 
                  'brand',
                  'quantity'
                  )


class CreateProductSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Product_version
        fields = (
                  'title', 
                  'product', 
                  'price',
                  'discount',
                  'property_value',
                  )
    

class ProductListSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    discount = DiscountSerializer()
    small_desc = serializers.CharField(source = 'product.small_desc')
    images = serializers.SerializerMethodField()

    def get_images(self, product):
        return ImageSerializer(product.images.filter(is_main=False), many=True).data

    class Meta:
        model = Product_version
        fields = (
                  'id',
                  'title',
                  'price',
                  'discount',
                  'small_desc',
                  'images',
                  )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCategory
        fields=('category_name','quantity')