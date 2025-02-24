from django.urls import path,include
from watchlist_app.api.views import (
    ReviewList,
    WatchListAV,
    ReviewDetail,
    WatchDetailAV,
    StreamPlatformAV,
    StreamDetailAV,
    StreamPlatformVS,
    ReviewCreate,
    StreamPlatform
)
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("<int:pk>", WatchDetailAV.as_view(), name="movie-detail"),

    path('',include(router.urls)),

    # path("stream/", StreamPlatformAV.as_view(), name="stream"),
    # path("stream/<int:pk>", StreamDetailAV.as_view(), name="streamplatform-detail"),

    path("<int:pk>/review-create/", ReviewCreate.as_view(), name="stream-detail"),
    path("<int:pk>/reviews/", ReviewList.as_view(), name="stream-detail"),
    path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]
