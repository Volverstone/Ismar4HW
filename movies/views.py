from django.views.generic import ListView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/list.html'
    context_object_name = 'movies'