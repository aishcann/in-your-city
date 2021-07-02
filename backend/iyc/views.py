from django.shortcuts import render
from django.db.models import query
from rest_framework import generics
from .serializers import EventSerializer
from .models import Event
from django.http import JsonResponse, HttpResponse


# Create your views here.

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# def event_list(request):
#     # only grab some attributes from our database, else we can't serialize it.
#     events = Event.objects.all().values('name', 'date', 'time', 'location', 'link', 'description','photo')
#     # convert our artists to a list instead of QuerySet
#     events_list = list(events)
#     # safe=False is needed if the first parameter is not a dictionary.
#     return JsonResponse(events_list, safe=False)


# def event_detail(request, pk):
#     event = Event.objects.get(id=pk)
#     return HttpResponse(event)
