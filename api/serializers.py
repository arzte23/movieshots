from rest_framework import serializers

from gallery.models import MediaItem, Screenshot


class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ["id", "image", "tags"]


class MediaItemSerializer(serializers.ModelSerializer):
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
