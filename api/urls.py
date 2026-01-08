from django.urls import path

from . import views

urlpatterns = [
    path("screenshots/", views.ScreenshotListAPI.as_view(), name="screenshot_list"),
]
