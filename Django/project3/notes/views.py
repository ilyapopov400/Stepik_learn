from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.

class Index(View):
    template_name = "notes/index.html"

    def get(self, request):
        return render(
            request=request, template_name=self.template_name
        )
