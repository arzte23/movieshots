from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from gallery.models import MediaItem, Screenshot


class ScreenshotSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Screenshot
        fields = ["id", "image", "tags"]


class MediaItemSerializer(serializers.ModelSerializer):
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
