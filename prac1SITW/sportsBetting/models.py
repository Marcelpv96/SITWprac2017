from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.TextField()

class Event(models.Model):
    name    = models.TextField()
    sport   = models.ForeingKey(Sport)
    local   = models.ForeingKey(Team)
    visitor = models.ForeingKey(Team)

class Team(models.Model):
    name = models.TextField()
    country = models.TextField()

class Bet(models.Model):
    user = models.ForeingKey(User)
    event = models.ForeingKey(Event)
