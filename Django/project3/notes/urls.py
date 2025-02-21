from django.urls import path
from . import views

app_name = "notes"
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add_note', views.AddNote.as_view(), name='add_note'),
    path('add_note/', views.AddNote.as_view(), name='add_note'),

]
