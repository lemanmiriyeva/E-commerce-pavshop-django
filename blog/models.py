from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils.text import slugify
from core.models import TimeStampedModel
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
User = get_user_model()



class BlogCategory(TimeStampedModel, models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'BlogCategories'
        ordering = ['-id'] 


class Blog (TimeStampedModel, models.Model):
    title = models.CharField(max_length=255)
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = RichTextField()
    slug = models.SlugField(null=True, blank=True, unique=True)
    tags = TaggableManager()
    img = models.ImageField(upload_to = 'blog_images', null=True, blank=True) 
    category = models.ForeignKey(BlogCategory, related_name = "blogs", on_delete = models.CASCADE, null=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save() 
    
    def hard_delete(self):
        super(Blog, self).delete()

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)

    def __str__(self) -> str:
        return f'id: {self.id} -- Blog by {self.title}'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self ).save(*args, **kwargs)


class Comment (TimeStampedModel):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    subject = models.TextField(default='Other')
    name=models.CharField(max_length=50)
    email=models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog= models.ForeignKey(Blog, related_name='comments',  on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self) -> str:
        return f' Comment by  {self.user_id}'
    
    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)


class BlogStatistic(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    comment_count =  models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.blog} - stats'











