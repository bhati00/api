from django.urls import path
from rest_auth.registration.views import ConfirmEmailView
from . import views

urlpatterns = [

    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
]
