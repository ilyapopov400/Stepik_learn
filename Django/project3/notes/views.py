from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse

from register import models as register_models
from .models import Notes


# Create your views here.

class Index(View):
    template_name = "notes/index.html"

    def get(self, request):
        if request.user.is_anonymous is False:
            notes_models = Notes
            notes_user = notes_models.objects.filter(user=request.user)
            content = {"notes": list(
                map(lambda x: x.note, notes_user)
            )}
        else:
            content = {"notes": None}

        return render(
            request=request, template_name=self.template_name, context=content
        )


class AddNote(View):
    """
    - добавление заметки в БД
    """
    template_name = "notes/add_note.html"
    template_name_redirect = "notes/index.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)

    def post(self, request):
        users_models = register_models.CustomUser
        notes_models = Notes()

        user = users_models.objects.get(username=request.user)
        notes_models.user = user
        notes_models.note = request.POST["note-text"]
        notes_models.save()

        notes_user = Notes.objects.filter(user=request.user)
        content = {"notes": list(
            map(lambda x: x.note, notes_user)
        )}

        return render(request=request, template_name=self.template_name_redirect, context=content)


class Note(View):
    """
    - просмотр одного поста пользователя
    """
    template_name = "notes/note.html"

    def get(self, request):
        content = {"note": "post of user"}
        return render(request=request, template_name=self.template_name, context=content)
