from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add/', views.AddBook.as_view(), name="add_book"),
]
