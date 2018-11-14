from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
	name = 'Jay'
	return render(request, "index/index.html", {'name' : name})


