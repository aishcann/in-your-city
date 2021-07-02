from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Event
        fields = ('id', 'name', 'date', 'time', 'location', 'link', 'description', 'photo')