from django.db import models
from .Enums.userType import UserType
import uuid


# Create your models here.
class User(models.Model):
    id = models.UUIDField(
        primary_key= True,
        default= uuid.uuid4,
        unique= True,
        editable= False
    )
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    user_type = models.IntegerField(choices= UserType.choices(), default= UserType.BUYER)
    is_active = models.BooleanField(default= True)
    wallet_balance = models.FloatField()
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self) :
        return self.id
    