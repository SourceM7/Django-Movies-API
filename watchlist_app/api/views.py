from rest_framework.response import Response
from watchlist_app.models import Movies
from watchlist_app.api.serializers import MoviesSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

class MovieListAV(APIView):

    def get(self,request):
        movies=Movies.objects.all()
        serializer = MoviesSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MovieDetailAV(APIView):

    def get(self,request,pk):
        try:
            movie=Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response({'Error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer=MoviesSerializer(movie)
        return Response(serializer.data)
    

    def put(self,request,pk):
        movie=Movies.objects.get(pk=pk)
        serializer=MoviesSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
            movie=Movies.objects.get(pk=pk)
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
    
