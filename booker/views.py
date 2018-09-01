from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .serializer import ReservationSerializer, RoomSerializer
from .models import Reservation
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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
        final_data = request.data
        del final_data['room_pk']
        reserv = Reservation(**final_data, room=obj)
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

    def can_schedule(meeting_data):
        pass

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