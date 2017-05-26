#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
import urllib2
import datetime


def generate_header(username, password, api_key):
    ssoid = login(api_key, username, password)
    header = {'X-Application': api_key,
              'X-Authentication': ssoid,
              'content-type': 'application/json',
              'accept': 'application/json'
              }
    return header


def callAping(url, request):
    try:
        req = urllib2.Request(url, request,
                              generate_header("guillem.orellana@gmail.com", "go147258369", "FHjLyss3VQbZfiMU"))
        response = urllib2.urlopen(req)
        jsonResponse = response.read()
        return json.loads(jsonResponse)

    except urllib2.URLError:
        print 'Oops there is some issue with the request'
        exit()
    except urllib2.HTTPError:
        print 'Oops there is some issue with the request' + urllib2.HTTPError.getcode()
        exit()


def getMarketCatalouge(eventId):
    if (eventId is not None):
        print 'Calling listMarketCatalouge Operation to get MarketID and selectionId'
        endPoint = 'https://api.betfair.com/exchange/betting/rest/v1.0/listMarketCatalogue/'
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        market_catalouge_req = '{"filter":{"eventIds":["' + str(eventId) + '"], "marketCountries":["GB"],' \
                                                                           '"marketStartTime":{"from":"' + now + '"}},"maxResults":"20" }'
        """
        print  market_catalouge_req
        """
        market_catalouge_response = callAping(endPoint, market_catalouge_req)

        return market_catalouge_response


def getEventsList(team_name):
    endPoint = 'https://api.betfair.com/exchange/betting/rest/v1.0/listEvents/'
    market_catalouge_req = '{"filter":{ "textQuery" : "' + team_name + '" }}'
    response = callAping(endPoint, market_catalouge_req)

    return response


def login(key, user, password):
    endpoint = "https://identitysso.betfair.es/api/login"

    header = {'X-Application': key, 'Accept': 'application/json'
              }

    url = endpoint + "?username=" + user + "&password=" + password

    response = requests.post(url, headers=header).text

    return json.loads(response)["token"]


def getMarketCatalouge(IDs):
    for ID in IDs:
        print getMarketCatalouge(ID)


def getEventsforTeam(Team):
    eventList = getEventsList(Team)
    events = []
    for event in eventList:
        events.append({'ID': event['event']['id'],
                       'Team1': event['event']['name'].split(' v ')[0],
                       'Team2': event['event']['name'].split(' v ')[1],
                       'Esport': 'Futbol'})
    return events
