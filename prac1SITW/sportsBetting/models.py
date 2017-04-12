from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Sport(models.Model):
    name = models.TextField(null=False)


class Event(models.Model):
    name = models.TextField(null=False)
    sport = models.ForeingKey(Sport)
    local = models.ForeingKey(Team)
    visitor = models.ForeingKey(Team)


class Team(models.Model):
    name = models.TextField(null=False)
    country = models.TextField()


class Bet(models.Model):
    user = models.ForeingKey(User)
    event = models.ForeingKey(Event)
