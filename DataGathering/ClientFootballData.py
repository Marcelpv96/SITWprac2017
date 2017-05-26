import requests
import json


class ClientFootballData(object):
    API_KEY = "1b53fb869db841c89fc2163344077637"
    BASE_URL = "http://api.football-data.org/v1/"
    SERVICES = {
        'competitions': 'competitions/',
        'team': 'teams/',
        'events': 'fixtures/'
    }

    @staticmethod
    def api_call(url):
        response = requests.get(url,
                                headers={
                                    'X-Auth-token': ClientFootballData.API_KEY,
                                    'X-Response-Control': 'full'
                                }).text
        return json.loads(response)

    @staticmethod
    def competitions(competition=-1):
        if competition == -1:
            # List all competitions
            return ClientFootballData.api_call(ClientFootballData.BASE_URL + \
                                               ClientFootballData.SERVICES['competitions'])
        else:
            return ClientFootballData.api_call(ClientFootballData.BASE_URL + \
                                               ClientFootballData.SERVICES['competitions'] + str(competition))

    @staticmethod
    def teams_competition(competition_id):
        return ClientFootballData.api_call(ClientFootballData.BASE_URL + \
                                           ClientFootballData.SERVICES['competitions'] + \
                                           str(competition_id) + "/teams")

    @staticmethod
    def team(team_id):
        return ClientFootballData.api_call(ClientFootballData.BASE_URL + \
                                           ClientFootballData.SERVICES['team'] + \
                                           str(team_id))

    @staticmethod
    def events(competition):
        return ClientFootballData.api_call(ClientFootballData.BASE_URL + \
                                           ClientFootballData.SERVICES['events'] + \
                                           "?league=" + competition)["fixtures"]
