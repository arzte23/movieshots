import uuid

from autoslug import AutoSlugField
from django.db import models
from django_countries.fields import CountryField
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

from .utils import get_file_path


class MediaItem(models.Model):
    TYPE_CHOICES = (
        ("MOVIE", "Movie"),
        ("SERIES", "TV Show"),
    )
    title = models.CharField(max_length=200)
    slug = AutoSlugField(unique=True, populate_from="title")
    media_type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    release_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    country = CountryField()

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    """A custom through model for tagging with UUID primary keys"""

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Screenshot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    media_item = models.ForeignKey(
        MediaItem, on_delete=models.CASCADE, related_name="screenshots"
    )
    image = models.ImageField(upload_to=get_file_path)
    tags = TaggableManager(through=UUIDTaggedItem)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Screenshot of {self.media_item.title}"
