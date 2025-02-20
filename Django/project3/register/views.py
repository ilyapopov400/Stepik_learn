from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.

class UserReg(View):
    template_name = "register/reg.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)

    def post(self, request):
        return HttpResponse("Вы прошли регистрацию")
