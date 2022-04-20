from rest_framework.viewsets import ModelViewSet
from tag.serializers import TagSerializer
from core.models import Tag


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
