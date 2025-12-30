from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("item/<slug:slug>/", views.media_detail, name="media_detail"),
    path("search/", views.search_results, name="search_results"),
    path(
        "movies/", views.category_view, {"category_type": "MOVIE"}, name="movies_list"
    ),
    path(
        "tv-shows/",
        views.category_view,
        {"category_type": "SERIES"},
        name="series_list",
    ),
    path(
        "screenshot/<uuid:pk>/favorite/", views.toggle_favorite, name="toggle_favorite"
    ),
    path("my-collection/", views.favorite_list, name="favorite_list"),
]
