from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]
