from rest_framework.response import Response
from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
 


class StreamPlatformAV(APIView):

    def get(self,request):
        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamDetailAV(APIView):
    def get(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        serializer=StreamPlatformSerializer(platform)
        return Response(serializer.data)


class WatchListAV(APIView):

    def get(self,request):
        movies=WatchList.objects.all()
        serializer = WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):

    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    

    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
            movie=WatchList.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    







# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movies=Movies.objects.all()
#         serializer=MoviesSerializer(movies,many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         serializer=MoviesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET','DELETE','PUT'])
# def movie_detail(request,pk):

#     if request.method=='GET':
#         try:
#             movie=Movies.objects.get(pk=pk)
#         except Movies.DoesNotExist:
#             return Response({'Error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
#         serializer=MoviesSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method=='PUT':
#         movie=Movies.objects.get(pk=pk)
#         serializer=MoviesSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#     if request.method=='DELETE':
#         movie=Movies.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
