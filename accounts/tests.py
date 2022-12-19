from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Country

class UserModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'first_name': 'Gunay',
            'username': 'Gun',
            'image': 'http://pavshop.my-style.in/demo/Single_Img_Demo/images/product-2-3.jpg',
            'phone': '05512345567',
            'address1': 'Adress1',
            'address2': 'Adress2',
            'town': 'Barcelona',
            'country': Country.objects.create(country_name = 'Spain', country_code = 'SP')
        }
        cls.user = User.objects.create(**cls.data)

    def test_create(self):
        user = User.objects.first()
        self.assertEqual(self.user, user)   

    def test_str(self):
        self.assertEqual(str(self.user), f"{self.data['first_name']} --- {self.data['username']}")

    @classmethod
    def tearDownClass(cls):
        pass 