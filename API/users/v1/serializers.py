from email.policy import default
import profile
from pyexpat import model
from attr import fields
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.models import User

from users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user_type','wallet_balance')
        
        
class UserSerializer(UserDetailsSerializer):
    
    profile = UserProfileSerializer(source = 'userProfile')  
      
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile',)
    
   
           
    def update(self, instance, validated_data):
        userprofile_serializer = self.fields['profile']
        userprofile_instance = instance.userProfile
        userprofile_data = validated_data.pop('userProfile', {})
        userprofile_serializer.update(userprofile_instance, userprofile_data)
        instance = super().update(instance, validated_data)
        return instance
  
class CustomRegisterSerializer(RegisterSerializer):

    first_name = serializers.CharField() 
    last_name = serializers.CharField()         
    profile = UserProfileSerializer(source = 'userProfile')  
    
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', '')
        }
       
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        UserProfile.objects.create(
                user=user,
                user_type=self.validated_data.get('user_type', 1),
                wallet_balance=self.validated_data.get('wallet_balance', 0.0)
            )
        return user