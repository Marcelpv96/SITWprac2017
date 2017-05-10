#!/usr/bin/env python
# -*- coding:utf-8 -*-

from docopt import docopt
import requests
import json
import urllib2
import datetime
import sys

doc = """
Usage:
    login.py -u <username> -p <password> -k <key> | --key=<key> --username=<username> --password=<password>
Options:
    -h --help                           Show this info. [default:None]
    -u USERNAME --username=USERNAME     Specify betfair username. [default:None]
    -p PASSWORD --password=PASSWORD     Specify betfair password. [default:None]
    -k KEY --key=KEY                    Specify the key [default:None]
"""


def callAping(url, request):
    try:
        req = urllib2.Request(url, request, header)
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
    if(eventId is not None):
        print 'Calling listMarketCatalouge Operation to get MarketID and selectionId'
        endPoint = 'https://api.betfair.com/exchange/betting/rest/v1.0/listMarketCatalogue/'
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        market_catalouge_req = '{"filter":{"eventIds":["' + str(eventId) + '"], "marketCountries":["GB"],'\
                                    '"marketStartTime":{"from":"' + now + '"}},"maxResults":"20" }'
        """
        print  market_catalouge_req
        """
        market_catalouge_response = callAping(endPoint, market_catalouge_req)

        return market_catalouge_response


def getEventsList(team_name):
    endPoint = 'https://api.betfair.com/exchange/betting/rest/v1.0/listEvents/'
    market_catalouge_req = '{"filter":{ "textQuery" : "'+ team_name +'" }}'
    response = callAping(endPoint, market_catalouge_req)

    return response


def login(key, user, password):
    endpoint = "https://identitysso.betfair.es/api/login"

    header =    { 'X-Application'   : key
                , 'Accept'          : 'application/json'
                }

    url = endpoint + "?username=" + user + "&password=" + password

    response = requests.post(url, headers=header).text

    return json.loads(response)["token"]



if __name__ == "__main__":
    API_KEY = docopt(doc)["--key"][0]
    USERNAME = docopt(doc)["--username"][0]
    PASSWORD = docopt(doc)["--password"][0]

    ssoid = login(API_KEY, USERNAME, PASSWORD)
    header = { 'X-Application': API_KEY,
                'X-Authentication': ssoid,
                'content-type': 'application/json',
                'accept': 'application/json'
                }

    print getEventsList("Real Madrid")
