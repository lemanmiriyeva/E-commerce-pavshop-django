from modeltranslation.translator import translator, TranslationOptions
from .models import Blog

class BlogsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Blog, BlogsTranslationOptions)

