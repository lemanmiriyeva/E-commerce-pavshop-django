from django.test import TestCase
from .models import ContactMessage

class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'full_name': 'Gunay',
            'email': 'gunay@gmail.com',
            'phone': '551234567',
            'subject': 'Message',
            'message': 'Something'
        }
        cls.contact = ContactMessage.objects.create(**cls.data)

    def test_create(self):
        contact = ContactMessage.objects.first()
        self.assertEqual(self.contact, contact)   

    def test_str(self):
        self.assertEqual(str(self.contact), self.data['subject'])

    @classmethod
    def tearDownClass(cls):
        pass 