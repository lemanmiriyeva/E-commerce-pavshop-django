from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Blog, BlogCategory

class BlogModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'title': 'New Blog',
            'user': User.objects.create(first_name= 'Gunay', username='Leman', image = 'http://pavshop.my-style.in/demo/Single_Img_Demo/images/product-2-3.jpg', address1 = 'address1', address2 = 'address2' , town = 'Baku'),
            'content': 'Something',
            'tags': 'newtag',
            'img': 'http://pavshop.my-style.in/demo/Single_Img_Demo/images/product-2-3.jpg',
            'category': BlogCategory.objects.create(title = 'furniture'),
        }
        cls.blog = Blog.objects.create(**cls.data)

    def test_create(self):
        blog = Blog.objects.first()
        self.assertEqual(self.blog, blog)   

    # def test_str(self):
    #     self.assertEqual(str(self.blog), f"id: {self.data['id']} -- Blog by {self.data['title']}")

    @classmethod
    def tearDownClass(cls):
        pass 