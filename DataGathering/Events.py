from ClientFootballData import ClientFootballData
from utilities import *

setup_django()

from sportsBetting.models import Team, Event
from django.contrib.auth.models import User

COMPETITIONS = ["PL",   # Premier League
                "BL1",  # BundesLiga
                "SA",   # Serie A
                "PD",   # Primera Division
                "FL1",  # Ligue 1
                "DED",  # Eredivise
                ]


def save_events():
    Event.objects.all().delete()
    for c in COMPETITIONS:
        for event in ClientFootballData.events(c):
            local = Team.objects.get(name=event["homeTeamName"])
            visitor = Team.objects.get(name=event["awayTeamName"])
            e = Event()
            e.name = local.short_name + ' v ' + visitor.short_name
            e.team1 = local
            e.team2 = visitor
            e.user = User.objects.get(username='admin')
            e.save()
