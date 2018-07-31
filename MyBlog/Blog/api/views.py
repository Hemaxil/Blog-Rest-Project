from Blog.models import Post
from django.db.models import Q
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter
from .permissions import IsOwnerOrReadOnly
from .serializers import PostListSerializer,PostDetailSerializer,PostCreateSerializer

class PostListAPIView(ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostListSerializer
    filter_backends=(SearchFilter,OrderingFilter,)
    search_fields=('title','content','user__username',)
    def get_queryset(self):
        queryset_list=Post.objects.all()
        query=self.request.GET.get("q")
        if query:
            queryset_list=queryset_list.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return queryset_list



class PostCreateAPIView(CreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostCreateSerializer
    permission_classes=(IsAuthenticated,)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class PostDetailAPIView(RetrieveUpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializer
    #changing the lookup field to slug since by default its pk
    lookup_field="slug"

class PostUpdateAPIView(UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostCreateSerializer
    permission_classes=(IsAuthenticated,IsOwnerOrReadOnly,)
    #changing the lookup field to slug since by default its pk
    lookup_field="slug"

    def perform_update(self,serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializer
    permission_classes=(IsAuthenticated,IsOwnerOrReadOnly,)
    #changing the lookup field to slug since by default its pk
    lookup_field="slug"
