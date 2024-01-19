from rest_framework import serializers
from base.models import Item


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'