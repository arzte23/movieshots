from django.shortcuts import get_object_or_404, render

from .models import MediaItem, Screenshot


def home(request):
    recent_screenshots = Screenshot.objects.select_related("media_item").order_by(
        "-created_at"
    )[:20]

    return render(request, "gallery/home.html", {"screenshots": recent_screenshots})


def media_detail(request, slug):
    item = get_object_or_404(MediaItem, slug=slug)
    images = item.screenshots.all()

    return render(
        request, "gallery/media_detail.html", {"item": item, "images": images}
    )
