
from DataGathering import utilities

utilities.setup_django()

from sportsBetting.models import Event
from sportsBetting.models import Team


def save_event(event):

    if not Event.objects().get(api_id=event["ID"]):
        # Add event
        new_Event = Event()
        new_Event.api_id = int(event["ID"])
        new_Event.name = event['team1'] + ' v ' + event['team2']
        new_Event.team1 = Team.objects.filter(short_name__exact=event['team1'])
        new_Event.team2 = Team.objects.filter(short_name__exact=event['team2'])
        new_Event.save()


