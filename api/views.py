from rest_framework import generics

from gallery.models import MediaItem

from .serializers import MediaItemSerializer


class MediaItemListAPI(generics.ListAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer
