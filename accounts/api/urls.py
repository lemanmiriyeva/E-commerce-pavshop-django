from django.urls import path
from .views import MyTokenObtainPairView
from .views import SubscriberEmailView, RegisterApi


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('subscribe/', SubscriberEmailView.as_view(), name='subscribe' ),
    path('register/',RegisterApi.as_view()),
]