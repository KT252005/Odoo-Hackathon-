from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser  # Adjusted import path based on your app structure
from .serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # Corrected to use CustomUser model
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
