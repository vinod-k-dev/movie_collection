from django.urls import path
from .api_views import CollectionDetailView, CollectionView, MovieListView

from .middleware import ResetRequestCounter, RequestCountView

urlpatterns = [
    path(
        "collections/", CollectionView.as_view(), name="collection-list-create"
    ),
    path('collection/<uuid:collection_uuid>/', CollectionDetailView.as_view(), name='collection-detail'),
    path("request-count/", RequestCountView.as_view(), name="request-count"),
    path(
        "request-count/reset/",
        ResetRequestCounter.as_view(),
        name="reset-request-count",
    ),
    path("movies/", MovieListView.as_view(), name="movie-list"),
]
