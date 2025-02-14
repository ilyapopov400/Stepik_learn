from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from django.core.files.storage import FileSystemStorage


# Create your views here.
class Index(View):
    template_name = "user_app/index.html"

    def get(self, request):
        print("Hello index")
        return render(
            request=request, template_name=self.template_name
        )


def json_response(request):
    return JsonResponse({1: "Hello World!!!"})


class Hello(View):
    template_name = "user_app/hello.html"

    def get(self, request, name):
        context = {
            "name": name,
        }
        return render(request=request, template_name=self.template_name, context=context)


class Forms(View):
    template_name = "user_app/form.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)

    def post(self, request):
        data = request.POST
        print(request.POST)
        name = data['name']
        review = data['user_feedback']
        print(name, review)
        return redirect(to="hello_user", name=name)
        # return HttpResponse(f"Thank your for your answer, {name}")


class Download(View):
    template_name = "user_app/download_file.html"

    def get(self, request):
        return render(request=request, template_name=self.template_name)

    def post(self, request):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request=request, template_name=self.template_name, context={
                'uploaded_file_url': uploaded_file_url
            })
