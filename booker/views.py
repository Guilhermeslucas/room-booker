from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .serializer import ReservationSerializer, RoomSerializer
from .models import Reservation
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import dateutil.parser
#dateutil.parser.parse('2008-04-10 11:47:58-05')

# Create your views here.
class ReservationsListView(APIView):
    serializer_class = ReservationSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Reservation.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        room_pk = request.data['room_pk']
        obj = Room.objects.filter(pk=room_pk)
        if not(obj):
            return Response({"Status": "The room you are trying to book does not exists"}, status=status.HTTP_404_NOT_FOUND)
        if can_schedule(request.data):
            final_data = format_room_input(request.data)
            reserv = Reservation(**final_data, room=obj[0])
            reserv.save()
            return Response(status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk, format=None):
        obj = Reservation.objects.filter(pk=pk)
        if obj:
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, format=None):
        obj = Reservation.objects.filter(pk=pk).update(**request.data)
        if obj:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class RoomsListView(APIView):
    serializer_class = RoomSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Room.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk, format=None):
        obj = Room.objects.filter(pk=pk)
        if obj:
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, format=None):
        obj = Room.objects.filter(pk=pk).update(**request.data)
        if obj:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

def can_schedule(meeting_data):
        return True

def format_room_input(request_data):
    del request_data['room_pk']
    request_data['begin'] = dateutil.parser.parse(request_data['begin'])
    request_data['end'] = dateutil.parser.parse(request_data['end'])
    return request_data