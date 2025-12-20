from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import MediaItem, Screenshot


def home(request):
    recent_screenshots = Screenshot.objects.select_related("media_item").order_by(
        "-created_at"
    )[:20]

    return render(request, "gallery/home.html", {"screenshots": recent_screenshots})


def media_detail(request, slug):
    item = get_object_or_404(MediaItem, slug=slug)
    screenshots = item.screenshots.all()

    return render(
        request, "gallery/media_detail.html", {"item": item, "screenshots": screenshots}
    )


def search_results(request):
    query = request.GET.get("q")
    screenshots = []

    if query:
        screenshots = Screenshot.objects.filter(
            Q(media_item__title__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()

    return render(
        request,
        "gallery/search_results.html",
        {
            "screenshots": screenshots,
            "query": query,
        },
    )
