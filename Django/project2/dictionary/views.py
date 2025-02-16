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
        word1, word2 = request.POST["word1"].lower(), request.POST["word2"].lower()
        add_word = utils.BaseEngin()
        add_word.write(word1=word1, word2=word2)
        return redirect(to="home")


class ShowWords(View):
    template_name = "dictionary/show_words.html"

    def get(self, request):
        db = utils.BaseEngin()
        words = db.read()
        context = {"words": words}

        return render(request=request, template_name=self.template_name, context=context)
