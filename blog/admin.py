# from modeltranslation.admin import TranslationAdmin
from django.contrib.admin import SimpleListFilter
from django.contrib import admin
from .models import *
admin.site.register(BlogStatistic)
admin.site.register(BlogCategory)
# admin.site.register(Comment)


class TagFilter(SimpleListFilter):
    title = 'Tags Filter'
    parameter_name = 'blogTag'  

    def lookups(self, request, model_admin):
        return (
           ( 'has_tag', 'has_tag'),
           ( 'no_tag', 'no_tag')
        )

    def queryset(self, request, queryset) :
        if not self.value():
            return queryset
        if self.value().lower() == 'has_tag':
            return queryset.exclude(blogTag__isnull=True)  
        if self.value().lower() == 'no_tag':
            return queryset.exclude(blogTag__isnull=False)


@admin.register(Blog)
class blogAdmin(TranslationAdmin):
    list_filter=[ "created_at", TagFilter]
    list_display= ['id','title', 'category','user', 'created_at' ]  
    search_fields = ['user', 'slug', 'tag']
    list_max_show_all = 10
    list_per_page = 10


class CommentAdmin(admin.ModelAdmin):
    list_display=('user','name', 'email', 'blog','subject','body')
    list_filter = ('active',)
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment,CommentAdmin)





