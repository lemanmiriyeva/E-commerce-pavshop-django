from .serializers import BlogListSerializer, CreateBlogSerializer
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http import Http404
from blog.models import Blog




class BlogReadUpdateDeleteView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)  

    def get(self,request, *args,   pk=None, **kwargs):
        if pk:
            blog_ = get_object_or_404(Blog, id=pk)
            return Response(BlogListSerializer(blog_).data)
        blogs = Blog.objects.all()

        blog_list = BlogListSerializer(blogs, many=True, context ={'request': request} ).data
        print(request)
        return Response(blog_list)
    
    def post(self, request):
        print(request.data)
        new_blog = CreateBlogSerializer(data = request.data, context = {'request': request})
        if new_blog.is_valid():
            new_blog.save()
            return Response(new_blog.data)
        return Response(new_blog.errors, status=404)

    def put(self, request, pk=None, *args, **kwargs):
        blog_ = get_object_or_404(Blog, id=pk)
        blog_Serializer = CreateBlogSerializer(data = request.data, instance=blog_)
        if blog_Serializer.is_valid():
            blog_Serializer.save()
            return Response(BlogListSerializer(blog_).data)
        return Response(blog_Serializer.errors, status=404)
        
    def patch(self, request,  *args, **kwargs):
        pk = kwargs['pk']
        blog = get_object_or_404(Blog, id=pk)
        blog_data = request.data
        blog_serializer = BlogListSerializer(data = blog_data, instance=blog, partial=True)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return Response(BlogListSerializer(blog).data)
        return Response(blog_serializer.errors, status=404)
    
    def delete(self, request, pk, *args, **kwargs):
        blog_= Blog.objects.filter(pk=pk)
        if not blog_.exists():
            raise Http404
        blog_ = blog_.first()
        blog_.soft_delete()
        return Response(status=204)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
        