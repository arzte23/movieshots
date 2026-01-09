from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from gallery.models import MediaItem, Screenshot

from .serializers import MediaItemDetailSerializer, ScreenshotSerializer


class ScreenshotListAPI(generics.ListAPIView):
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
    ordering_fields = ["created_at", "likes_count"]

    def get_queryset(self):
        queryset = (
            Screenshot.objects.select_related("media_item")
            .annotate(likes_count=Count("favorites"))
            .all()
        )
        is_favorited = self.request.query_params.get("is_favorited")
        if is_favorited == "true" and self.request.user.is_authenticated:
            queryset = queryset.filter(favorites=self.request.user)

        return queryset


class MediaItemDetailAPI(generics.RetrieveAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemDetailSerializer
    lookup_field = "slug"


class ScreenshotLikeAPI(APIView):
    serializer_class = ScreenshotSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        screenshot = get_object_or_404(Screenshot, pk=pk)
        user = request.user
        if user in screenshot.favorites.all():
            screenshot.favorites.remove(user)
            return Response(
                {"status": "unliked", "likes_count": screenshot.favorites.count()},
                status=status.HTTP_200_OK,
            )
        else:
            screenshot.favorites.add(user)
            return Response(
                {"status": "liked", "likes_count": screenshot.favorites.count()},
                status=status.HTTP_201_CREATED,
            )
