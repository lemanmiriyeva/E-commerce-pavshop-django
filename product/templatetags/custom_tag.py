from django.template.defaulttags import register
from product.models import Product_version, PropertyValue


@register.simple_tag
def get_product_count():
    return Product_version.objects.all().count()


@register.simple_tag
def get_all_colors():
    return PropertyValue.objects.filter(property__title = 'color')





