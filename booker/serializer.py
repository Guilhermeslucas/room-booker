from rest_framework import serializers
from .models import Reservation, Room


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        depth = 1
        fields = ['begin','end', 'title', 'room', 'pk']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        depth = 1
        fields = ['name','level', 'pk']