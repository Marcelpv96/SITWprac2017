from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sport(models.Model):
    name = models.CharField(null=False, max_length=100)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(null=False, max_length=100)
    crest = models.ImageField(upload_to="crests/")

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(null=False, max_length=100)
    sport = models.ForeignKey(Sport)
    team1 = models.ForeignKey(Team, null=True, related_name='local')
    team2 = models.ForeignKey(Team, null=True, related_name='visitor')

    def __unicode__(self):
        return self.name


class Bet(models.Model):
    quota = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    description = models.TextField(null=True)
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.event.name + " - " + str(self.user)
