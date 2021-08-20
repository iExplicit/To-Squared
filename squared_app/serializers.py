from rest_framework import serializers
from .models import Squared


class SquaredSerializer(serializers.ModelSerializer):
    ''' Serializer to map the Todo model to JSON. '''

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Squared
        fields = ('id', 'title', 'description', 'done', 'created_at', 'user')
        read_only_fields = ('created_at', 'id')
