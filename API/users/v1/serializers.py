from dataclasses import fields
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','password','user_type','is_active','wallet_balance','created_at','updated_at')
        extra_kwargs = {'password': {'write_only': True}}
       