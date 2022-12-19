from distutils.command.upload import upload
from django.db import models
from datetime import date
from blog.models import BlogStatistic
from core.models import TimeStampedModel
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.text import slugify
from django.urls import reverse_lazy
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


class Brand (TimeStampedModel, models.Model):
    brand = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f'{self.brand}'


class Discount(TimeStampedModel, models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.CharField(max_length=255)
    is_percent = models.BooleanField(default=True)
    amount = models.IntegerField()

    def __str__(self) -> str:
        if self.is_percent == True:
            return f'{self.name} - {self.amount}%'
        else:
            return f'{self.name} - {self.amount}AZN'


class Designer (models.Model):
    designer = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.designer
   

class ProductCategory(TimeStampedModel):
    category_name = models.CharField(max_length=255, unique=True)
  
    class Meta:
        verbose_name_plural = 'productCategories'

    def __str__(self):
        return self.category_name



class Product (TimeStampedModel, models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name = 'category')
    small_desc = models.TextField()
    large_desc = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)
    desc = RichTextField(null=True, blank= True)
    info = RichTextField(null=True, blank= True)


class Property(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title


class PropertyValue(models.Model):
    title = models.CharField(max_length=50)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    code = models.CharField(null=True, blank=True, default='FF0000', max_length=15)

    def __str__(self):
        return f'{self.title}--{self.code}'


class Product_version (TimeStampedModel, models.Model):
    title = models.CharField(max_length=50, default='')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=True, related_name='versions')
    code = models.CharField(max_length=20, unique=True,  null=True, blank=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True, default=None)
    designer= models.ForeignKey(Designer, on_delete=models.CASCADE, default=True)
    tags = TaggableManager()
    slug = models.SlugField(null=True, blank=True, unique=True)
    property_value = models.ManyToManyField(PropertyValue, related_name='reng')

    def __str__(self):
        return f'{self.code} - {self.title}'
    

class Image(models.Model):
    img = models.ImageField(upload_to = 'product_images')
    product = models.ForeignKey(Product_version, related_name='images',  on_delete=models.CASCADE )
    is_main = models.BooleanField (default = False )

    def __str__(self):
        return f'Image of {self.product.title}'


class Rating (models.Model):
    point = models.IntegerField()


class Review(TimeStampedModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product_version = models.ForeignKey(Product_version, on_delete=models.CASCADE, null=True, related_name='reviews')
    comment = models.TextField(max_length=250, default='')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product_version.title}--{self.comment}'


# class Wishlist(models.Model):
#     product_version = models.ForeignKey(Product_version, on_delete = models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.product_version} is liked by {self.user}'


class ProductReviewStatic(TimeStampedModel, models.Model):
    product_version = models.ForeignKey(Product_version, on_delete=models.CASCADE, null=True)
    review_count =  models.PositiveIntegerField(default=0)
    rating_count = models.PositiveBigIntegerField(default=0)
    avg_rating = models.FloatField(default=0)

    def __str__(self) -> str:
        return f'{self.product_version} - stats'
