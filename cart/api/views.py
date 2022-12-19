from rest_framework.views import APIView
from cart.models import WishlistModel, Basket, Basket_item
from product.models import Product_version
from .serializers import WishlistSerializer, BasketSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
class WishlistAPI(APIView):
    queryset = WishlistModel.objects.all()
    serializers_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        obj = WishlistModel.objects.filter(user_id=self.request.user).all()
        print(obj)
        serializers = self.serializers_class(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product = Product_version.objects.filter(id=product_id).first()
        exist_wish_product = WishlistModel.objects.filter(user_id = request.user, wished_item = product)
        if exist_wish_product.exists():
            print("bu userde artiq bu element wishlistdedir")
            message = {'success': True, 'message' : 'This product has already been added'}
            return Response(message, status = status.HTTP_302_FOUND)
        else:
            if product:
                wishlist = WishlistModel(user_id = request.user, wished_item = product)
                wishlist.save()
                message = {'success': True, 'message' : 'Product added to your wishlist.'}
                return Response(message, status = status.HTTP_201_CREATED)
            message = {'success' : False, 'message': 'Product not found.'}
            return Response(message, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        if ProductID:
            WishlistModel.objects.filter(user_id = self.request.user, wished_item=ProductID).first().delete()
        return Response(status = status.HTTP_200_OK)
class BasketAPI(APIView):
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        obj = Basket.objects.filter(user_id = self.request.user, is_active = True).all()
        serializer = self.serializer_class(obj, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        quantity = request.data.get('quantity')
        product_id = request.data.get('product')
        product = Product_version.objects.filter(id=product_id).first()
        exist_basket_product = Basket_item.objects.filter(user_id = request.user, product_id = product)
        if exist_basket_product.exists():
            print("Bu userde artiq bu element basketdedir")
            message = {'success': True, 'message' : 'This product has already been added to cart'}
            return Response(message, status = status.HTTP_302_FOUND)
        else:
            if product:
                basket_item = Basket_item(user_id = request.user, product_id = product)
                basket_item.quantity += int(quantity)
                basket_item.save()
                basket = Basket(user_id = request.user, is_active = True, b_item_id = basket_item)
                basket.save()
                message = {'success': True, 'message' : 'Product added to your card.'}
                return Response(message,status = status.HTTP_201_CREATED)
            message = {'success' : False, 'message': 'Product not found.'}
            return Response(message, status = status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        ProductID = request.data.get('product')
        if ProductID:
            user_basket_item = Basket_item.objects.get(product_id = ProductID, user_id = request.user)
            user_basket = Basket.objects.get(b_item_id=user_basket_item, user_id = request.user )
            user_basket.delete()
            user_basket_item.delete()
            message = {'success': True, 'message' : 'Product deleted'}
            return Response(message,status = status.HTTP_200_OK)
        message = {'success' : False, 'message': 'Product not found.'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)