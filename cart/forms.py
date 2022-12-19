from django import forms 
from .models import Shipping_info, Billing_detail


class billingForm(forms.ModelForm):
    
    class Meta:
        model = Billing_detail
        exclude = ['shipping_address',]

        
class shippingForm(forms.ModelForm):

    class Meta:
        model = Shipping_info
        fields = "__all__"
        


