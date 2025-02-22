from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from register import models as register_models


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
        users = register_models.CustomUser
        notes = register_models.Notes
        data = request.POST
        new_note = data["note"]
        user_username = request.user
        print(new_note, user_username)

        return render(request=request, template_name=self.template_name)
