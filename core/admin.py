from django.contrib import admin
from .models import *

admin.site.register(Adress)
admin.site.register(Contanct_info)
admin.site.register(Team)
admin.site.register(Sponsor)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display= ['full_name','subject' ]  
    search_fields = ['full_name', 'subject', 'email']
    list_max_show_all = 10
    list_per_page = 2