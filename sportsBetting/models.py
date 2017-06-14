from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Team(models.Model):
    name = models.CharField(null=False, max_length=100)
    short_name = models.CharField(null=True, max_length=100)
    crest = models.ImageField(upload_to="crests/", null=True)
    created_by = models.ForeignKey(User, null=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/teams/list_teams"


class Competition(models.Model):
    name = models.CharField(null=False, max_length=100)
    short_name = models.CharField(null=True, max_length=100)
    teams = models.ManyToManyField(Team)
    logo = models.ImageField(upload_to="competitions/", null=True)
    user = models.ForeignKey(User, null=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/competitions/list_competitions"


class Event(models.Model):
    name = models.CharField(null=False, max_length=100)
    user = models.ForeignKey(User)
    team1 = models.ForeignKey(Team, null=True, related_name='local')
    team2 = models.ForeignKey(Team, null=True, related_name='visitor')

    def __unicode__(self):
        return self.name


    def get_absolute_url(self):
        return "/events/list_events"


class Bet(models.Model):
    quota = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    description = models.TextField(null=True)
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.event.name + " - " + str(self.user)

    def get_absolute_url(self):
        return '/bets/list_bets'

class Review(models.Model):
    RATING_CHOICES	= ((1,	'one'),	(2,	'two'),	(3,	'three'),	(4,	'four'),	(5,	'five'))
    rating	= models.PositiveSmallIntegerField('Rating	(stars)',	blank=False,	default=3,	choices=RATING_CHOICES)
    comment	= models.TextField(blank=True,	null=True)
    user	= models.ForeignKey(User,	default=1)

    class Meta:
        abstract = True

class TeamReview(Review):
    team = models.ForeignKey(Team)

    class Meta:
        unique_together	= ("team",	"user")
