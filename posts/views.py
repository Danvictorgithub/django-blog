from rest_framework import generics, permissions
# Create your views here.

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadonly
class PostList(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadonly ,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadonly ,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer