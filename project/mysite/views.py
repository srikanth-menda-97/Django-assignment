from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from .models import Candidate, Experience, Education

def index(request,candidate_id):
	candidate = Candidate.objects.get(pk=candidate_id)
	experience =  Experience.objects.filter(candidate_id=candidate_id)
	education =  Education.objects.filter(candidate_id=candidate_id)
	similar_candidates = Candidate.objects.exclude(pk=candidate_id)
	print()
	context = {'candidate': candidate, 'experience':experience, 'education':education, 'similar_candidates': similar_candidates }	
	return render(request, 'mysite/index.html', context)

