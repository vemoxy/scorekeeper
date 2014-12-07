from django.shortcuts import render

from scorelib import score_manager
from scorelib import match_manager

def index(request):
	return render(request, 'index.html')

def match(request, match_id):
	match = match_manager.get_match(match_id)
	return render(request, 'match.html', match)