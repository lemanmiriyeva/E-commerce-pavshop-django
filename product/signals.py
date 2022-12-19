from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Product_version, ProductReviewStatic, Review
import time


@receiver(post_save, sender=Product_version)
def code_func(sender, instance, created , *args, **kwargs ):
    if created:
        code = f'{instance.product.category.category_name[0:3]}-{time.strftime(r"%d%M-%H%S", time.localtime())}'
        instance.code = code 


@receiver(post_save, sender=Product_version)
def slug_func(sender, instance, created,  *args, **kwargs ):
    # if created:
        slug = slugify(f'{instance.title}- {instance.code}' )
        if not slug == instance.slug:
            instance.slug = slug 
            instance.save()


@receiver(post_save ,sender=Product_version)
def post_save_func(sender, instance, created,  *args, **kwargs):
    if created:
        ProductReviewStatic.objects.create( product_version = instance )


@receiver(post_save ,sender=Review)
def post_save_func(sender, instance, created,  *args, **kwargs):
    if created:
        print(instance.product_version)
        count_object = ProductReviewStatic.objects.get(product_version=instance.product_version)
        count_object.review_count = count_object.review_count + 1
        count_object.rating_count = count_object.rating_count + int(instance.rating)
        count_object.avg_rating = instance.rating/instance.review_count
        count_object.save()