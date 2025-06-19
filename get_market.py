# Export active markets in polymarkets data
# Decode the data using json files
# Return the outcomePrices and id values of a market 

import requests
import json

url = "https://gamma-api.polymarket.com/markets"

querystring = {"active":"true", "closed":"false"}

response = requests.request("GET", url, params=querystring)

markets = response.json

for market in markets:
    market_id = market.get("id")
    outcomeprices = market.get("outcomePrices", "[]")
    print(market_id, outcomeprices)