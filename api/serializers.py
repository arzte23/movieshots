from rest_framework import serializers

from gallery.models import Screenshot


class ScreenshotSerializer(serializers.ModelSerializer):
    movie_slug = serializers.ReadOnlyField(source="media_item.slug")
    media_type = serializers.ReadOnlyField(source="media_item.media_type")

    class Meta:
        model = Screenshot
        fields = ["id", "image", "created_at", "movie_slug", "media_type"]
