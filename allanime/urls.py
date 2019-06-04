from django.urls import path
from . import views

urlpatterns = [
	path('', views.all_anime_quotes, name='all_anime_quotes'),
]