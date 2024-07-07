from django.urls import path
from dj_rest_auth.registration.views import VerifyEmailView
from . import views

urlpatterns = [
    path('account-confirm-email/<str:key>/', VerifyEmailView.as_view()),
]
