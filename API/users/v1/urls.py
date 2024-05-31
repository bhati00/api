from django.urls import path
from dj_rest_auth.registration.views import ConfirmEmailView
from . import views

urlpatterns = [

    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('users/delete/<int:pk>', views.DeleteUser.as_view(), name= "users")
]
