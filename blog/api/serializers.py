from rest_framework import serializers, status
from blog.models import Blog

class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
                    'id', 
                    'title', 
                    'tags', 
                    'category',
                    )
                    
    def validate(self, data):
        request = self.context['request']
        data['user'] =  request.user
        return super().validate(data) 

class BlogListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return f"Username = {obj.user.username}"
   
    class Meta:
        model = Blog
        fields = (
                    'id',
                    'user',
                    'title', 
                    'category',
                    'tags', 
                    )