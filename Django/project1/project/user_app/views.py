from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    print("Hello index")
    return HttpResponse("<h2>Hello index</h2>")


def about(request):
    print("Hello about")
    return HttpResponse("<h2>Hello about</h2>")


def year_archive(request, year: int):
    return HttpResponse("<h3>Today is {} year</h3>".format(year))


def json_response(request):
    return JsonResponse({1: "Hello World!!!"})


def hello(request, name):
    context = {
        "name": name.capitalize(),
    }
    template = "hello.html"
    return render(request=request, template_name=template, context=context)
