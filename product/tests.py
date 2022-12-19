from django.test import TestCase
from .models import PropertyValue, Property

class PropertyValueModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'title': 'red',
            'property': Property.objects.create(title='color'),
            'code': 'FFFF00'
        }
        cls.property_value = PropertyValue.objects.create(**cls.data)

    def test_create(self):
        property_value = PropertyValue.objects.first()
        self.assertEqual(self.property_value, property_value)   

    def test_str(self):
        self.assertEqual(str(self.property_value), f"{self.data['title']}--{self.data['code']}")

    @classmethod
    def tearDownClass(cls):
        pass 