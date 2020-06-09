from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "generator/home.html", {'password': 'hwerea898kasdf!@asdlfkj'})


def eggs(request):
    return HttpResponse("Eggs")