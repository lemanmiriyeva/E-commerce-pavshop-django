from django.urls import path
from .views import  BlogList, BlogDetail, TagBlogList, SearchBlog, CommentView

urlpatterns =[

    path('blog-detail/<slug:slug>', BlogDetail.as_view(), name = 'blog-detail'),
    path('blog-list/', BlogList.as_view(), name = 'blog_list'),
    path('tags/<slug:tag_slug>/', TagBlogList.as_view(), name = 'posts_by_tag'),
    path('search/', SearchBlog.as_view(), name = 'search_blog'),
    path('submit_comment/<int:blog_id>',CommentView,name='submit_comment'),


]
    