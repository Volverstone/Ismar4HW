from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie, Profile
from .forms import MovieForm, RegisterForm, ProfileForm


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')
        genres = self.request.GET.getlist('genres')

        if search:
            queryset = queryset.filter(title__icontains=search)

        if category:
            queryset = queryset.filter(category__id=category)

        if genres:
            queryset = queryset.filter(genres__id__in=genres).distinct()

        return queryset


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_create.html'
    success_url = reverse_lazy('movie_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_update.html'
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movies/movie_delete.html'
    success_url = reverse_lazy('movie_list')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'movies/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'movies/login.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('movie_list')


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'movies/profile.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'movies/profile_update.html'
    success_url = reverse_lazy('movie_list')
