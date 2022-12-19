from rest_framework.test import APITestCase
from django.urls import reverse, resolve
from rest_framework.authtoken.models import Token
from rest_framework import status
from product.models import Product_version


class ListCreateProductViewTest(APITestCase):
    products_urls = reverse('products')

    def setUP(self):
        self.product  = Product_version.objects.create(title= 'new product', product= 1, price= 12, tags= 'newtag', property_value=1)
        self.token = Token.objects.create(product = self.product)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token' + self.token.key)

    def tearDown(self):
        pass

    def test_get_products_authenticated (self):
        response = self.client.get(self.products_urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_products_unauthenticated (self):
    #     self.client.force_authenticate(product=None, token = None )
    #     response = self.client.get(self.products_urls)
    #     self.assertEqual(response.status_code, 401)
    
    # def test_post_product_authenticated(self):
    #     data = {
    #         'title': 'new', 
    #         'product': 1, 
    #         'price': 23, 
    #         'tags' : 'tag', 
    #         'property_value': 1
    #     }
    #     response = self.client.post(self.products_urls, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data['title'], 'new')

