from django.urls import path
from . import views

urlpatterns = [
    path('users/register', views.UserCreate.as_view(), name= "create"),
]
