from django.db import models
from product.models import Product_version
from accounts.models import Country
from core.models import TimeStampedModel
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
User = get_user_model()


class Promocode (TimeStampedModel, models.Model):
    promocode = models.CharField(max_length=8)
    is_active = models.BooleanField(default=True)
    is_percent = models.BooleanField(default=True)
    discount = models.IntegerField()

    def __str__(self):
        return f'{self.promocode}--created at: {self.created_at}'



class WishlistModel(models.Model):
    is_active = models.BooleanField(default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_item = models.ForeignKey(Product_version, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user_id}'s - wishlist"
        
class Basket_item(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    product_id = models.ForeignKey(Product_version, on_delete = models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.user_id}'s {self.product_id.title}'s basket item"
    def get_total(self):
        total = self.product_id.new_price * self.quantity
        return total

class Basket(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # b_item_id = models.ManyToManyField(Basket_item, related_name="basket_items")
    b_item_id = models.ForeignKey(Basket_item, on_delete = models.CASCADE, related_name="basket_items", null= True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    def __str__(self):
        return f"{self.user_id}'s basket"

class Cart (TimeStampedModel, models.Model):
    cart_number = models.IntegerField()
    cvv_code = models.CharField(max_length=3)
    expiration_date = models.DateField()
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    @admin.display(description="Customer's  phone number")
    def display_customer_phone(self):
        return format_html(f'<font color="red">{ self.user.phone}</font>')

    def __str__(self) :
        return f'{self.cart_number} - {self.expiration_date}'

 
class Billing_detail (TimeStampedModel, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255) 
    town = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    shipping_address = models.ForeignKey('Shipping_info',on_delete=models.CASCADE,  blank=True,  null=True)


class Shipping_info (TimeStampedModel, models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True) 
    town = models.CharField(max_length=150, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    

class Payment_method (TimeStampedModel, models.Model):
    method = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)

    
class OrderStatus(TimeStampedModel):
    is_ordered = models.BooleanField(default=False)
    is_shipped =  models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)


class Order(TimeStampedModel):
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    total_price = models.FloatField()