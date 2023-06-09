from rest_framework import viewsets
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]



