from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.views.generic import View, CreateView, TemplateView
from .models import Team, Sponsor
from product.models import Product_version
from blog.models import Blog
from django.db.models import Q


class Homeview(View):
    def get(self,request):
        return render(request, 'index.html', {})
    

class about(TemplateView):
    template_name = 'about-us.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Team.objects.all()
        context['sponsors'] = Sponsor.objects.all()
        return context


class contact(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact'

    
class Search(View):
    model = Product_version

    def post(self, request):
        searched = request.POST['searched']
        blogs = Blog.objects.filter(Q(title__contains = searched) | Q(user__first_name__contains = searched))
        products = Product_version.objects.filter(Q(title__contains = searched) | Q(code__contains = searched)| Q(designer__designer__contains = searched))
        print('blogs:',blogs)
        print('products', products)
        if blogs:
            messages.success(request,f"Blogs for {searched}.")
            return render(request, 'blog-list.html', {'blogs': blogs})
        elif products:
            messages.success(request,f"Products for {searched}.")
            return render(request, 'product-list.html', {'products': products})
        else:
            print('blogs:',blogs)
            print('products', products)
            messages.warning(request,f"There aren't any result for {searched}.")
            return render(request, 'homepage')