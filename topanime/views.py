from django.shortcuts import render

# Create your views here.
def top_anime_quotes(request):
	return render(request, 'topanime/top_anime_quotes.html', {})