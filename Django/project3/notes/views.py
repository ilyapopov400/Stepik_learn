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


class AddNote(View):  # TODO
    """
    - добавление заметки в БД
    """
    template_name = "notes/add_note.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)

    def post(self, request):
        data = request.POST
        new_note = data["note"]
        user = request.user
        print(new_note, user)

        return render(request=request, template_name=self.template_name)
