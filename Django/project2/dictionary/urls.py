from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('/', views.Home.as_view(), name='home'),
    path('home/', views.Home.as_view(), name='home'),
    path('/home', views.Home.as_view(), name='home'),
    path('add_word/', views.AddWord.as_view(), name='add_word'),
    path('/add_word', views.AddWord.as_view(), name='add_word'),
    path('words_list/', views.ShowWords.as_view(), name='show_words'),
    path('/words_list', views.ShowWords.as_view(), name='show_words'),

]
