from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("blog/<int:year>/", views.year_archive),
    path("json/", views.json_response),
    path("hello/<str:name>", views.hello),
]
