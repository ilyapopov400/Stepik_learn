from django.urls import path
from . import views

app_name = "register"
urlpatterns = [
    path('reg/', views.UserReg.as_view(), name='reg'),
    path('reg', views.UserReg.as_view(), name='reg'),

]
