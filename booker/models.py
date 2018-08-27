from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField()

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    begin = models.DateTimeField('begin date')
    end = models.DateTimeField('end date')
    title = models.CharField(max_length=200)