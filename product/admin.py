from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.contrib.admin import SimpleListFilter
from .models import *

admin.site.register(Brand)
admin.site.register(Designer)
admin.site.register(Image)
admin.site.register(Property)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(ProductReviewStatic)


class ProductCategoryAdmin(TranslationAdmin):
    pass

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ImageInlineAdmin(admin.TabularInline):
    model = Image


class discountFilter(SimpleListFilter):
    title= "Filter by discount"
    parameter_name= 'discount'

    def lookups(self, request, model_admin):
        return (
            ('has_discount', 'has_discount'),
            ('no_discount','no_discount')
        )
    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() =='has_discount':
            return queryset.exclude(discount__isnull =True)
        if self.value().lower() == 'no_discount':
            return queryset.filter (discount__isnull=True )
        

@admin.register(Product_version)
class ProductVersionAdmin(admin.ModelAdmin):
    list_filter = [discountFilter]
    list_display= ['id','title', 'code','designer' ]  
    inlines = (ImageInlineAdmin, )   
    search_fields = ('title', 'code', 'designer', 'quantity', )
    prepopulated_fields = {'slug':['title',]}


@admin.register(PropertyValue)
class PropertyValueAdmin(admin.ModelAdmin):
    list_display= ['id','title', 'property','code' ]  
    search_fields = ('code', 'title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['id','category', 'brand']  
    search_fields = ('category', 'brand',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    search_fields = ('name', 'amount',)