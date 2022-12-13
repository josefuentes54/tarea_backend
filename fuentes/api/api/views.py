from rest_framework.viewsets import ModelViewSet
from api.models import Post
from api.api.serializers import PostSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()