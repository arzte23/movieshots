from django.urls import path

from . import views

urlpatterns = [
    path("screenshots/", views.ScreenshotListAPI.as_view(), name="screenshot_list"),
    path(
        "items/<slug:slug>/",
        views.MediaItemDetailAPI.as_view(),
        name="media_item_detail",
    ),
    path(
        "screenshots/<uuid:pk>/like/",
        views.ScreenshotLikeAPI.as_view(),
        name="screenshot_like",
    ),
]
