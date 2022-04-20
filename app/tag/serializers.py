from rest_framework.serializers import ModelSerializer

from core.models import Tag


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'created_on']
        extra_kwargs = {
            'created_on': {
                'read_only': True
            }
        }
