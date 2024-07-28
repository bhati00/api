from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import uuid
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

from .Enums.userType import UserType

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    

# class UserProfile(models.Model):
#     REQUIRED_FIELDS = []
#     USERNAME_FIELD = "user_guid"
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userProfile")
#     user_guid = models.UUIDField(
#         default=uuid.uuid4,
#         unique=True,
#         editable=False
#     )
#     user_type = models.IntegerField(choices=UserType.choices(), default=UserType.BUYER)
#     wallet_balance = models.FloatField()
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['created_at' ]  # Corrected the ordering syntax
        


