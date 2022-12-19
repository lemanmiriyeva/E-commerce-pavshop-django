from rest_framework import serializers
from cart.models import WishlistModel
from cart.models import Basket, Basket_item
from product.api.serializers import ListProductSerializers


class WishlistSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField()
    image = serializers.CharField()
    title = serializers.CharField()
    price = serializers.CharField()
    quantity = serializers.CharField()
    class Meta:
        model = WishlistModel
        fields = ['id', 'user_id', 'image', 'title', 'price', 'quantity']
class BasketItemSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user_id.username')
    # product_id = ListProductSerializers()
    product_id = serializers.CharField(source='product_id.title')
    class Meta:
        model = Basket_item
        fields = ['id', 'user_id', 'quantity', 'product_id']
class BasketSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user_id.username')
    b_item_id = BasketItemSerializer()
    class Meta:
        model = Basket
        fields = ['id', 'user_id', 'is_active', 'b_item_id']