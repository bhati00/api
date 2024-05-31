from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import uuid

from .Enums.userType import UserType

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userProfile")
    user_guid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    user_type = models.IntegerField(choices=UserType.choices(), default=UserType.BUYER)
    wallet_balance = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at' ]  # Corrected the ordering syntax

