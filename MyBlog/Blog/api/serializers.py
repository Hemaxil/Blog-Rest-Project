from rest_framework.serializers import ModelSerializer
from Blog.models import Post

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=('title','content','publish')

class PostListSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=('id','user','title','slug','content','image','draft','publish')
# fields=['title','content','image','draft','publish',]

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=('title','slug','content','publish')
