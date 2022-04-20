from rest_framework.serializers import ModelSerializer

from core.models import Recipe


class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'price', 'tags', 'uploaded_by']
        extra_kwargs = {
            'uploaded_by': {
                'read_only': 'True'
            }
        }

