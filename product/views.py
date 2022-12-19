from django.shortcuts import redirect
from .models import Brand, Product_version, ProductCategory, Image, Product, ProductReviewStatic
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ReviewForm
from .models import Review
from accounts.tasks import send_mail_to_subscribers
from django.contrib.auth import get_user_model
User = get_user_model()
import datetime
# date = datetime.date.today()
# start_week = date - datetime.timedelta(date.weekday())
# end_week = start_week + datetime.timedelta(7)
# entries = Product_version.objects.filter(created_at__range=[start_week, end_week])


class BlogListMixin(object):
    def get_context_data(self,**kwargs):
        context= super(BlogListMixin, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['tags'] = Product_version.tags.most_common()[0:2]
        context['brands'] = Brand.objects.all()
        return context


class BrandBlogList(BlogListMixin,ListView):
    model = Product_version
    context_object_name = 'products'
    template_name = 'product-list.html'

    def get_queryset(self) :
                queryset = Product_version.objects.filter(product__brand__brand=self.kwargs.get('brand_brand'))
                print( 'queryset::',queryset)
                return queryset


class TagBlogList(BlogListMixin,ListView):
    model = Product_version
    context_object_name = 'products'
    template_name = 'product-list.html'

    def get_queryset(self):
        queryset = Product_version.objects.filter(tags__slug = self.kwargs.get('tag_slug'))
        return queryset


class ColorBlogList(BlogListMixin,ListView):
    model = Product_version
    context_object_name = 'products'
    template_name = 'product-list.html'

    def get_queryset(self):
        queryset = Product_version.objects.filter(property_value__title = self.kwargs.get('color'))
        return queryset


class ProductDetail(DetailView):
    model = Product_version
    template_name = 'product-detail.html'
    context_object_name = 'product'
    
    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            context['images'] = Image.objects.all().filter(product__id =context['product'].id)
            context['colors'] = context['product'].property_value.filter(property__title = 'color').values()
            context['form'] = ReviewForm()
            context['reviews'] = Review.objects.filter(product_version__id = context['product'].id)
            context['relatedimg'] = Image.objects.filter(is_main=True)
            context['related'] = Product_version.objects.filter(product__category__id = context['product'].product.category.id).exclude(id=context['product'].id)[:4]
            return self.render_to_response(context)
        except Http404:
            messages.warning(request, "There aren't any product for your searching!")
            return redirect('/')

            
class ProductList(BlogListMixin, ListView):
    model = Product_version
    template_name = "product-list.html"
    context_object_name= 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        category_name = self.request.GET.get('category')
        if category_name:
            queryset = Product_version.objects.filter(product__category__category_name=category_name)
        else:
            queryset = Product_version.objects.all()
        return queryset


# def test(request):
#     print('+++')
#     send_mail_to_subscribers.delay()
#     return HttpResponse('testing')


class unlike_product_view(DetailView):
    template_name = 'wishlist.html'
    context_object_name = 'product'
    def get(self, request, id, *args, **kwargs):
        if 'liked_products' in request.session:
            if id not in set(map(int,  self.request.session.get('liked_products', '').split())):
                request.session['liked_products'] = f'{request.session.get("liked_products", "")}{id} '
            else:
                request.session['liked_products'] = (request.session['liked_products']).replace(str(id), '')
        else:
            request.session['liked_products'] = f'{request.session.get("liked_products", "")}{id} '
        return redirect(reverse_lazy('wishlist'))

        
class like_product_view(DetailView):
    context_object_name = 'product'
    def get(self, request, id, *args, **kwargs):
        if 'liked_products' in request.session:
            if id not in set(map(int,  self.request.session.get('liked_products', '').split())):
                request.session['liked_products'] = f'{request.session.get("liked_products", "")}{id} '
            else:
                request.session['liked_products'] = (request.session['liked_products']).replace(str(id), '')
        else:
            request.session['liked_products'] = f'{request.session.get("liked_products", "")}{id} '
        return redirect(reverse_lazy('product_list'))

class like_products_view(ListView):
    template_name = 'wishlist.html'
    context_object_name = 'products'
    model = Product_version

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(is_main=True)
        liked_products = set(map(int,  self.request.session.get('liked_products', '').split()))
        context['liked_product_list'] = Product_version.objects.filter(id__in = liked_products)
        return (context)


def ReviewView(request, product_id):
    product = Product_version.objects.get(id=product_id)
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        user_id = request.user.id
        review = Review(user=User.objects.get(id=user_id), rating = rating,  comment=comment , product_version=product)
        review.save()
    return redirect('product_detail', slug= product.slug)





