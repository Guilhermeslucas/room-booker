from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField()
    description = models.CharField(max_length=200, default='')

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    begin = models.IntegerField()
    end = models.IntegerField()
    title = models.CharField(max_length=200, default='')