from django import template
register = template.Library()
from product.models import Product_version
from django.contrib.auth import get_user_model
User = get_user_model()


@register.filter('test_filter')
def test_filter_funct(value, arg):
    return f'{value}{arg}'


@register.simple_tag(name='simple_tag')
def simple_tag_funct(arg1):
    return User.objects.all().count()+arg1


@register.inclusion_tag( filename='show_latest_products.html')
def show_latest_products( ):
    latest_products = Product_version.objects.all()
    print(latest_products)
    return {
        'latest_products': latest_products
    }