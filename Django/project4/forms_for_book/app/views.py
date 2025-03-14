from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from . import models
from . import forms


# Create your views here.

class Index(View):
    template_name = "app/index.html"

    def get(self, request):
        books = list()
        for book in models.Books.objects.all():
            books.append((book.author, book.title))
        context = {"books": books}

        return render(request=request, template_name=self.template_name, context=context)


class AddBook(View):
    template_name = "app/add_book.html"

    def get(self, request):
        form = forms.BookForm()
        context = {'form': form}
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request):
        form = forms.BookForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(to='app:index')
        else:
            form = forms.BookForm()
        context = {'form': form}
        return render(request=request, template_name=self.template_name, context=context)
