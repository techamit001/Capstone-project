
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	numbers = {
	0 : 'zero',
	1 : 'one',
	2 : 'two'
	}
	name = 'Jay'
	return render(request, "index/dashboard.html", {'name' : name, 'nums' : numbers})
