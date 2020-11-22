from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello Django!")

def name(request,year):
    return HttpResponse(year)

def myyear(request,year):
    return render(request,'yearview.html')