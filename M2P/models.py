from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User(models.Model):
    userNickname = models.CharField(max_length=100)
    userName = models.CharField(max_length=200)
    userMail = models.EmailField()

    def __str__(self):
        return self.userName


class Sport(models.Model):
    sportName = models.CharField(max_length=100)


    def __str__(self):
        return self.sportName


class Location(models.Model):
    locationName = models.CharField(max_length=200)
    locationAddress = models.CharField(max_length=200)
    sports = models.ForeignKey(Sport, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.locationName


class DateTime(models.Model):
    dateTime = models.DateTimeField(primary_key=True)

    def __str__(self):
        return self.dateTime


class Event(models.Model):
    eventName = models.CharField(max_length=100)
    sportId = models.ForeignKey(Sport, on_delete=models.CASCADE)
    dateTime = models.ForeignKey(DateTime, on_delete=models.CASCADE)
    idLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def _str_(self):
        return self.eventName


class Friendship(models.Model):
    creator = models.ForeignKey(User, related_name="friendship_creator_set", on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name="friend_set",on_delete=models.CASCADE)

    def _str_(self):
        return self.friend