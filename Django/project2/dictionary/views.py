from django.shortcuts import render, redirect
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
        add_word = utils.BaseEngin()
        # add_word.write(word1=word1, word2=word2)
        add_word.read()
        return redirect(to="home")
