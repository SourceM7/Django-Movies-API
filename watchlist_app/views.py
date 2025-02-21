# from django.shortcuts import render
# from watchlist_app.models import Movies
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movies.objects.all()
#     data={
#         'movies':list(movies.values())
#         }
    
#     return JsonResponse(data)



# def movie_detail(request,pk):
#     movie = Movies.objects.get(pk=pk)
#     data={
#         'movies':movie.name,
#         'descrption':movie.description,
#         'active':movie.active
#         }
#     return JsonResponse(data)