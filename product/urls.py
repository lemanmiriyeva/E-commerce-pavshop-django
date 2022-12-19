from django.urls import path
from .views import  ProductList, ProductDetail, like_product_view, like_products_view, unlike_product_view, TagBlogList, BrandBlogList, ColorBlogList, ReviewView

urlpatterns=[ 
    path('product-detail/<slug:slug>', ProductDetail.as_view(), name = 'product_detail'),
    path('product-list/', ProductList.as_view(), name='product_list'),
    path('liked-products/<int:id>/', like_product_view.as_view(), name='liked_product'),
    path('unliked-products/<int:id>/', unlike_product_view.as_view(), name='unliked_product'),
    path('wishlist/', like_products_view.as_view(), name='wishlist'),
    path('tags/<slug:tag_slug>', TagBlogList.as_view(), name='products_by_tag'),
    path('brand/<slug:brand_brand>', BrandBlogList.as_view(), name='products_by_brand'),
    path('color/<slug:color>', ColorBlogList.as_view(), name='products_by_color'),
    path('submit_review/<int:product_id>', ReviewView, name='submit_review'),
    # path('tester/', test, name='test')

    ]
   
