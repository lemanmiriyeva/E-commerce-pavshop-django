from django.urls import path 
from .views import cart, checkout_view

urlpatterns = [ 
    path('cart/', cart.as_view(), name = 'cart'),
    path('checkout/', checkout_view.as_view(), name = 'check_out' ),

]
   