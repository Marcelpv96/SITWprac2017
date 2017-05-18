from Betfair.BetfairClient import getEventsforTeam
from DataGathering import utilities

utilities.setup_django()

from sportsBetting.models import Event, Sport
from sportsBetting.models import Team


def save_event(event):

    if not Event.objects().get(api_id=event["ID"]):
        # Add event
        team = Team.objects.get(id=id).short_name
        event = getEventsforTeam(team)

        #for event in events:
        new_Event = Event()
        new_Event.api_id = int(event['ID'])
        new_Event.name = event['Team1'] + ' v ' + event['Team2']
        new_Event.team1 = Team.objects.get(short_name=event['Team1'])
        new_Event.team2 = Team.objects.get(short_name=event['Team2'])
        new_Event.sport = Sport.objects.get(id=1)
        new_Event.save()


