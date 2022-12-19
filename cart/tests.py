from django.test import TestCase
from .models import Promocode

class PromocodeModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'promocode': '1806',
            'discount': 10,
        }
        cls.promocode = Promocode.objects.create(**cls.data)

    def test_create(self):
        promocode = Promocode.objects.first()
        self.assertEqual(self.promocode, promocode)   

    # def test_str(self):
    #     self.assertEqual(str(self.promocode), f"{self.data['promocode']}--created at: {self.data['created_at']}")

    @classmethod
    def tearDownClass(cls):
        pass 