from django.contrib import admin
from .models import *
from django.contrib.admin import SimpleListFilter

admin.site.register(
                        [Basket_item, 
                        Promocode, 
                        Basket,
                        Shipping_info, 
                        Billing_detail, 
                        Payment_method, 
                        OrderStatus, 
                        Order]
                        )


class CardNumberFilter(SimpleListFilter):
    title = 'CardNumber Filter'
    parameter_name = 'mailll'
    def lookups(self, request, model_admin):
        return (
           ( 'has_mail', 'has_mail'),  
           ( 'no_mail', 'no_mail')
        )
    def queryset(self, request, queryset) :
        if not self.value():
            return queryset
        if self.value().lower() == 'has_mail':   
            return queryset.exclude(mail='')
        if self.value().lower() == 'no_mail':
            return queryset.filter(mail='')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display= ['id','cart_number', 'cvv_code','display1_customer_phone', '__str__' , ]  
    list_filter= ['cart_number', 'cvv_code', CardNumberFilter]
    search_fields = ['cart_number', 'cvv_code', 'user__first_name']
    list_editable= [ 'cvv_code',  ] 
    list_max_show_all = 10
    list_per_page = 2
    fieldsets=[
        ("Cart details", {
            'fields':(
                "cart_number", 'cvv_code'
                )
        }),
        ('Cart Date info',{
            'fields':('expiration_date',
            )
        }),
        ('Customer info',{
            'fields':('user',),
        })
    ]  
    

    @admin.display(description='Additional column')
    def display1_customer_phone(self, obj):
        return format_html('<font color="red">{}</font>', obj.user.phone )   #bu format_html-dir.
        

admin.site.site_title= "Pavshopun admin paneli"
admin.site.site_header= "Pavshop's admin panel"
admin.site.index_title= "Pavshop's site administration"




