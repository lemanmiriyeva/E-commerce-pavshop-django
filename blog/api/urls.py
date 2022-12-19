from .functionalviews import BlogReadUpdateDeleteView, BlogViewSet
from .views import BlogListGeneric, BlogRetreiveUpdateDelete
from rest_framework.routers import DefaultRouter
from django.urls import include
from django.urls import path
router = DefaultRouter()
router.register(r'viewset', BlogViewSet, basename='blogs')


urlpatterns = [
    path('blogs/', BlogReadUpdateDeleteView.as_view()),
    path('blogs/<int:pk>', BlogReadUpdateDeleteView.as_view()),
    path('generic/', BlogListGeneric.as_view()),  
    path('generic/<int:pk>', BlogRetreiveUpdateDelete.as_view()),  
    path('', include(router.urls))
]


