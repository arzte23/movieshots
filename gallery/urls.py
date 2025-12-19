from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("item/<slug:slug>/", views.media_detail, name="media_detail"),
]
