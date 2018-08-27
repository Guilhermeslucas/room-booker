from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField()

class Reservation(models.Model):
    room = models.IntegerField()
    begin = models.IntegerField()
    end = models.IntegerField()
    title = models.CharField(max_length=200, default='')