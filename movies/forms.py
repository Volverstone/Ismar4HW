from django import forms
from .models import Movie, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'image', 'category', 'genres']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
