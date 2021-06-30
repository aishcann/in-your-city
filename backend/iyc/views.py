from django.shortcuts import render
from django.db.models import query
from rest_framework import generics
from .serializers import EventSerializer
from .models import Event


# Create your views here.

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
