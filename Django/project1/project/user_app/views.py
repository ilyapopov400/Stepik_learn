from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    print("Hello index")
    return HttpResponse("Hello index")


def about(request):
    print("Hello about")
    return HttpResponse("Hello about")
