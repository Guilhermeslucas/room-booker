from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .serializer import ReservationSerializer, RoomSerializer
from .models import Reservation
from .models import Room
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
def index(request):
    m = Room.objects.create(name="aurora", level="1")
    m = Room.objects.filter(name="aurora")
    print(m[0].name)
    return HttpResponse("All ok")

class ReservationsListView(APIView):
    serializer_class = ReservationSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Reservation.objects.all(), many=True)
        return Response(serializer.data)

class RoomsListView(APIView):
    serializer_class = RoomSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Room.objects.all(), many=True)
        return Response(serializer.data)