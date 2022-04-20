from rest_framework.viewsets import ModelViewSet
from recipe.serializers import RecipeSerializer
from core.models import Recipe


class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def perform_create(self, serializer):
        # Pass on the kwargs user_profile explicitly, rest of the things serializer will take care.
        serializer.save(uploaded_by=self.request.user)