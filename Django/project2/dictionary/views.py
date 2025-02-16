from django.shortcuts import render
from django.views import View
from . import utils


# Create your views here.

class Home(View):
    template_name = "dictionary/home.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)


class AddWord(View):
    template_name = "dictionary/add_word.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)

    def post(self, request):

        word1, word2 = request.POST["word1"], request.POST["word2"]
        add = utils.AddWord(word1=word1, word2=word2)()
        return render(request=request, template_name=self.template_name)
