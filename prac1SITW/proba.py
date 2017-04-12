import requests
import json

url = "https://api.betfair.com/exchange/betting/json-rpc/v1"
header = {'X-Application': 'fYnUlGOraS6QFPFn', 'X-Authentication':
          'lcGHVC6KNCsffqWL7LGAFZU56frS0ENTPcG6W0JOkSA=', 'content-type': 'application/json'}

jsonrpc_req = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listMarketCatalogue", "params": {"filter":{ MarketFilter }}, "id": 1}'

response = requests.post(url, data=jsonrpc_req, headers=header)

print json.dumps(json.loads(response.text), indent=3)
