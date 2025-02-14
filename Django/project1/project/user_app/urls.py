from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path("forma/", views.Forms.as_view(), name="forma"),
    path("json/", views.json_response, name="json"),
    path("hello/<str:name>", views.Hello.as_view(), name="hello_user"),
    path("download/", views.Download.as_view(), name="download"),
]
