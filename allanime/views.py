from django.shortcuts import render

# Create your views here.
def all_anime_quotes(request):
	return render(request, 'allanime/all_anime_quotes.html', {})