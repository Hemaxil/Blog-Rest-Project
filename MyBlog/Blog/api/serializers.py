from rest_framework.serializers import ModelSerializer
from Blog.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields=('title','slug','content','image','draft','publish')
# fields=['title','content','image','draft','publish',]
