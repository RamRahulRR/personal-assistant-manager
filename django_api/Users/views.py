from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]  #[IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
