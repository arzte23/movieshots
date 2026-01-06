from django.urls import path
from . import views


urlpatterns = [
    path("items/", views.MediaItemListAPI.as_view(), name="media_item_list"),
]