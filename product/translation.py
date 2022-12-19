from modeltranslation.translator import translator, TranslationOptions
from .models import ProductCategory

class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ["category_name"]

translator.register(ProductCategory, ProductCategoryTranslationOptions)