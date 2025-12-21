from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import MediaItem, Screenshot


def home(request):
    screenshots_list = Screenshot.objects.select_related("media_item").order_by(
        "-created_at"
    )
    paginator = Paginator(screenshots_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "gallery/home.html", {"page_obj": page_obj})


def media_detail(request, slug):
    item = get_object_or_404(MediaItem, slug=slug)
    screenshots = item.screenshots.all()

    return render(
        request, "gallery/media_detail.html", {"item": item, "screenshots": screenshots}
    )


def search_results(request):
    query = request.GET.get("q")
    screenshot_list = []

    if query:
        screenshot_list = Screenshot.objects.filter(
            Q(media_item__title__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()

    paginator = Paginator(screenshot_list, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "gallery/search_results.html",
        {
            "page_obj": page_obj,
            "query": query,
        },
    )
