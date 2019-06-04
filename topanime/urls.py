from django.urls import path
from . import views

urlpatterns = [
	path('', views.top_anime_quotes, name='top_anime_quotes'),
]