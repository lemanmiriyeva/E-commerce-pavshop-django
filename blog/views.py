from django.views import View
from .forms import CommentForm
from django.db.models import Q
from .models import Blog, Comment
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, DetailView
User=get_user_model()


class TagMixin(object):
    def get_context_data(self,**kwargs):
        context= super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Blog.tags.most_common()[0:2]
        return context
        

class BlogList(TagMixin, ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog-list.html'
    # paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_blogs'] = Blog.objects.all().order_by('created_at')[:3]
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        category_title = self.request.GET.get('category')
        if category_title:
            queryset = Blog.objects.filter(category__title=category_title)
        return queryset
    

class BlogDetail(TagMixin,DetailView):
    model = Blog
    context_object_name = "blog"
    template_name = "blog-detail.html"
    form_class = CommentForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_blogs'] = Blog.objects.all().order_by('created_at')[:3]
        context['comments'] = Comment.objects.all()
        context['form'] = CommentForm()
        context['related'] = Blog.objects.filter(category__id = context['blog'].category.id).exclude(id=context['blog'].category.id)[:4]
        return context
    

class TagBlogList(TagMixin,ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog-list.html'

    def get_queryset(self):
        queryset = Blog.objects.filter(tags__slug = self.kwargs.get('tag_slug'))
        return queryset


class SearchBlog(View):
    model = Blog

    def post(self, request):
        searched = request.POST['searched']
        blogs = Blog.objects.filter(Q(title__contains = searched) | Q(user__first_name__contains = searched))
        if blogs:
            messages.success(request,f"Blogs for {searched}.")
        else:
            messages.warning(request,f"There aren't any result for {searched}.")
        return render(request, 'blog-list.html', {'blogs': blogs})
    

def CommentView(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    form=CommentForm(request.POST or None)
    if form.is_valid():
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        body=request.POST.get('body')
        user_id=request.user.id
        comment=Comment(user=User.objects.get(id=user_id),name=name,email=email,subject=subject,body=body,blog=blog)
        comment.save()

    return redirect('blog-detail',slug=blog.slug)
