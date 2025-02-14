from django.shortcuts import render
from django.views import View


# Create your views here.

class Home(View):
    template_name = "dictionary/home.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)
