from rest_framework import serializers

from gallery.models import MediaItem, Screenshot


class ScreenshotSerializer(serializers.ModelSerializer):
    movie_slug = serializers.ReadOnlyField(source="media_item.slug")
    media_type = serializers.ReadOnlyField(source="media_item.media_type")

    class Meta:
        model = Screenshot
        fields = ["id", "image", "created_at", "movie_slug", "media_type"]


class MediaItemDetailSerializer(serializers.ModelSerializer):
    screenshots = ScreenshotSerializer(many=True, read_only=True)

    class Meta:
        model = MediaItem
        fields = [
            "id",
            "title",
            "slug",
            "media_type",
            "release_year",
            "end_year",
            "description",
            "country",
            "screenshots",
        ]
