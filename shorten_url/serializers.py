import os
from typing import Dict

from django.conf import settings
from rest_framework import serializers

from shorten_url.models import ShortUrlModel


class ShortUrlField(serializers.Field):
    """
    Used to serialize a short id string, but to deserialize the short id with
    the base URL site included.
    """

    def to_representation(self, obj: 'ShortUrlModel') -> str:
        """Deserializing"""

        return os.path.join(settings.SITE_URL, obj.short_url)

    def to_internal_value(self, short_url: str) -> Dict:
        """Serializing"""

        if not short_url:
            raise serializers.ValidationError('This field may not be blank.')
        if len(short_url) != ShortUrlModel.ID_LENGTH:
            raise serializers.ValidationError(
                f'Ensure this field has no more than {ShortUrlModel.ID_LENGTH} characters.'
            )

        return {'short_url': short_url}


class ShortUrlSerializer(serializers.Serializer):
    short_url = ShortUrlField(source='*')
    url = serializers.URLField(required=True)
    created_at = serializers.DateTimeField(read_only=True)
    count = serializers.IntegerField(read_only=True)

    def create(self, validated_data: Dict) -> 'ShortUrlModel':
        """Overwrite method to use self.save() on the serializer directly."""
        return ShortUrlModel.objects.create(**validated_data)
