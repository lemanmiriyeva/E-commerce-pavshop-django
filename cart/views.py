import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from .forms import shippingForm, billingForm
from django.views.generic import View
from .models import Basket,Basket_item



class cart(ListView):
    template_name = 'shopping-cart.html'
    def get(self, request):
        return render(request, self.template_name)


class checkout_view(View):
    form_class = {
                    'billing': billingForm,
                    'shipping': shippingForm
                }
    template_name = 'checkout.html'
    success_url = '/'

    def get(self, request):
        shform = self.form_class['billing']
        bform = self.form_class['shipping']
        return render (request, self.template_name, {'shform': shform, 'bform': bform})

    def post(self,request):
        shform = shippingForm(request.POST)
        bform =  billingForm(request.POST)
        if shform.is_valid() or bform.is_valid():
            shform.save()
            bform.save()
            messages.success(request,f'Your info send to db ')
            return redirect('check_out')
        else:
            messages.error(request, ('Included information is false! Please enter right info!'))
            return render(request, 'checkout.html', {'shform': shform, 'bform': bform})

class BasketView(LoginRequiredMixin,ListView):
    model=Basket
    template_name='shopping-cart.html'
    def get_context_data(self, **kwargs):
        context=super(BasketView,self).get_context_data(**kwargs)
        context['user_basket']=Basket.objects.filter(user=self.request.user,is_active=True).all()
        total_price=0
        products=Basket_item.objects.filter(user=self.request.user,basket_items__is_active=True)
        for product in products:
            total_price += product.get_total()
        context['total_price']=total_price


        return context
