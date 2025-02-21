from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse

from . import utils
from . import models


# Create your views here.

class UserReg(View):
    template_name = "register/reg.html"
    template_name_redirect = "notes/index.html"
    template_name_bad_redirect = "register/bad_reg.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)

    def post(self, request):
        result = request.POST
        username = result["username"]
        first_name = result["first_name"]
        last_name = result["last_name"]
        email = result["email"]
        password1 = result["password1"]
        password2 = result["password2"]

        verification = utils.CleanDate(username, first_name, last_name, email, password1, password2)
        if verification():
            user = models.CustomUser()
            user.create_user(username, first_name, last_name, email, password1)
            # user = authenticate(request, username=username, password=password1)
            login(request, user)

        else:
            return render(request=request, template_name=self.template_name_bad_redirect)

        return render(request=request, template_name=self.template_name_redirect)


class Logout(View):
    template_name = "register/logout.html"
    template_name_redirect = "notes/index.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)

    def post(self, request):
        logout(request)
        return render(request=request, template_name=self.template_name_redirect)
