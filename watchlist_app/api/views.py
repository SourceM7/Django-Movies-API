from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import (
    WatchListSerializer,
    StreamPlatformSerializer,
    ReviewSerializer,
)
from rest_framework import viewsets

# from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadyOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle
from watchlist_app.api.throttling import ReviewCreateThrottle,ReviewListThrottle

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    throttle_classes=[ReviewCreateThrottle]
    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        movie = WatchList.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(
            watchlist=movie, review_user=review_user
        )

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data["rating"]
        else:
            movie.avg_rating = (
                movie.avg_rating + serializer.validated_data["rating"]
            ) / 2
        movie.number_rating = movie.number_rating + 1
        movie.save()
        serializer.save(watchlist=movie, review_user=review_user)


class ReviewList(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ReviewListThrottle,AnonRateThrottle]

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadyOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope='review-detail'


class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer



class StreamPlatformAV(APIView):
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(
            platform, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform, context={"request": request})
        return Response(serializer.data)


class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)