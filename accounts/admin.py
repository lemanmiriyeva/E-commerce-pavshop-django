from django.contrib import admin
from .models import Country, SubscriberEmail
from django.contrib.auth import get_user_model
User = get_user_model()
admin.site.register(Country)
admin.site.register(SubscriberEmail)





@admin.register(User)
class CartAdmin(admin.ModelAdmin):
    list_display= ['id','phone', 'first_name','last_name' ]  
    list_filter= ('country' , )
    search_fields = ['phone', 'town', 'country']
    list_max_show_all = 10
    list_per_page = 2