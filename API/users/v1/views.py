from users.models import User
from .serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework import generics
# Create your views here.

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"
    
    
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


        
    
   
    
