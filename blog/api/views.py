from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CreateBlogSerializer, BlogListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from blog.models import Blog

class BlogListGeneric(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = CreateBlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['category', ]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return super().get_serializer_class()
        else:
            return BlogListSerializer


class BlogRetreiveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = CreateBlogSerializer