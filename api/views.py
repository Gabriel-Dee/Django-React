from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# Where we woll write all of our endpoints

# The below code returns a list of different roooms
class RoomView(generics.CreateAPIView):
    querySet = Room.objects.all()
    serializer_class = RoomSerializer
