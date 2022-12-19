"""pavshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
# from core.views import index_view
# from core.views import about_us_view
# from blog.views import blog_detail_view
# from blog.views import blog_list_view
# from product.views import product_detail_view
# from product.views import product_list_view
# from cart.views import cart_view
# from user.views import login_view
# from user.views import register_view
# from cart.views import checkout_view
# from core.views import contact_view

urlpatterns = [
    # ... previously added endpoints
    path('openapi/', get_schema_view(
        title="Pavshop Service",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),


    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'), 
    

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path("i18n/", include("django.conf.urls.i18n")),
]




urlpatterns += i18n_patterns( 
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # path('about-us/', include('core.urls')),
    # path('blogs/', include('blog.urls')),
    path('blogs/', include('blog.urls')),
    path('api/', include('blog.api.urls')),
    path('api/', include('product.api.urls')),
    path('api/', include('accounts.api.urls')),
    path('api/', include('cart.api.urls')),
    path('products/', include('product.urls')),
    # path('api/', include('blog.api.urls')),
    # path('products/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('user/',include('accounts.urls') ),
    path('social-auth/', include('social_django.urls', namespace='social')),
    # path('user/', include('user.urls')),
    # path('cart/', include('cart.urls') ),
    # prefix_default_language=False    #Bunu yazsaq default olan language ucun http://127.0.0.1:8000/lan_code yazmadan yeni http://127.0.0.1:8000/ bu halda enter etdikde ozu lang_code artirmayacaq avtomatik sonuna
)

# urlpatterns += i18n_patterns(
#     path('', include('core.urls')))+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)



