from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from gallery.models import MediaItem, Screenshot

from .serializers import MediaItemDetailSerializer, ScreenshotSerializer


class ScreenshotListAPI(generics.ListAPIView):
    queryset = Screenshot.objects.select_related("media_item").all()
    serializer_class = ScreenshotSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "media_item__media_type": ["exact"],
    }
    search_fields = ["tags__name", "media_item__title", "media_item__description"]
    ordering_fields = ["created_at"]


class MediaItemDetailAPI(generics.RetrieveAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemDetailSerializer
    lookup_field = "slug"
