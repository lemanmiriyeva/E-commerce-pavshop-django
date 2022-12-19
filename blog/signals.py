from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Blog, BlogStatistic


@receiver(pre_save,sender=Blog)
def slug_generator_blog_model(sender,**kwargs):
    print("Request finished!")


@receiver(post_save ,sender=Blog)
def post_save_func(sender, instance, created,  *args, **kwargs):
    if created:
        BlogStatistic.objects.create( blog = instance )