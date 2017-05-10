from DataGathering.ClientFootballData import ClientFootballData
from DataGathering import utilities

utilities.setup_django()

from sportsBetting.models import Team

COMPETITIONS = ["PL",   # Premier League
                "BL1",  # BundesLiga
                "SA",   # Serie A
                "PD",   # Primera Division
                "FL1",  # Ligue 1
                "DED",  # Eredivise
                ]


def save_teams():
    Team.objects.all().delete()
    for competition in ClientFootballData.competitions():
        if competition['league'] in COMPETITIONS:
            for team in ClientFootballData.teams_competition(competition['id'])['teams']:
                new_team = Team()
                new_team.name = team["name"]
                new_team.short_name = team["shortName"]
                utilities.save_image_from_url(new_team.crest, team['crestUrl'])
                new_team.save()

