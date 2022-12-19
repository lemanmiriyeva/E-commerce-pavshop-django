from django.template.defaulttags import register
from product.models import Product, Image, Product_version
from django.db.models import Q

@register.filter
def get_range(value):
    return range(1, value+1)

@register.filter('count')
def count(category):
    return Product.objects.filter(category__id = category.id ).count()

@register.filter('split_filter')
def split_filter_funct(value):
    liked_products = map(int, value.split(' '))
    return liked_products
    

@register.filter('get_image')
def get_image(product_id):
    img = Image.objects.get(Q(product= product_id) & Q(is_main = True)  )
    return img.img.url



