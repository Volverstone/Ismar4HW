from django.contrib import admin
from .models import Movie, Category, Genre, Profile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'owner', 'created_at')
    list_filter = ('category', 'genres', 'created_at')
    search_fields = ('title',)
    filter_horizontal = ('genres',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
