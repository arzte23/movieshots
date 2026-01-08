from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from gallery.models import Screenshot

from .serializers import ScreenshotSerializer


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
