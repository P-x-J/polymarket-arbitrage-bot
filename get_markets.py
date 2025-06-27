import requests
import json
import re


def get_markets(gamma_api_data_url) -> list:
    querystring = {"active":"true", "closed":"false"}
    response = requests.request("GET", gamma_api_data_url, params=querystring)
    response = response.text
    response_json = json.loads(response)

    # Iterate over the json file and make a list with binary markets with decimal odds

    decoded_markets = []
 
    for market in response_json:
        outcome_prices = market.get("outcomePrices")
        outcome_prices_str = str(outcome_prices)
        match = re.search(r'\[\"([0-9]+\.[0-9]+)\", \"([0-9]+\.[0-9]+)\"\]', outcome_prices_str.strip())

        print (outcome_prices)
            
        if match:
        
            outcome_prices = []
            outcome_price1 = float(match.group(1))
            outcome_price2 = float(match.group(2))
            print(outcome_price1, outcome_price2)
            outcome_prices.append(outcome_price1)
            outcome_prices.append(outcome_price2)

            id = market.get("id")
            slug = market.get("slug")
            decoded_markets.append({"id": id, "outcomePrices": outcome_prices, "slug": slug})

    return decoded_markets
        



print(get_markets("https://gamma-api.polymarket.com/markets"))