from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from . import utils


# Create your views here.
class Index(View):
    template_name = "app/index.html"

    def get(self, request):
        utils.Logs()()
        return render(
            request=request, template_name=self.template_name
        )
