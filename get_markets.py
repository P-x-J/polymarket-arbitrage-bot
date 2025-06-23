import requests
import json



def main():
    get_events(get_markets())


def get_markets() -> list:
    # Export active markets in polymarkets data
    url = "https://gamma-api.polymarket.com/markets"

    # Use querystrings to list the market with various filtering and sorting options.
    querystring = {"active":"true", "closed":"false"}

    response = requests.request("GET", url, params=querystring)

    response = response.text

    response_json = json.loads(response)

    # Iterate over the json file and make a list with binary markets with decimal odds

    decoded_markets = []

    for market in response_json:
        try:
            outcome_price = market.get("outcomePrices")
            if outcome_price == None:
                pass
        except AttributeError:
            # Only add the events that have outcomeprices listed
            pass
        else:
            id = market.get("id")
            slug = market.get("slug")
            decoded_markets.append({"id": id, "outcomePrices": outcome_price, "slug": slug})

    return decoded_markets

def get_events(decoded_markets: list) -> list: 

    url = "https://gamma-api.polymarket.com/events"

    querystring = {"active":"true", "closed":"false"}

    response = requests.request("GET", url, params=querystring)

    response = response.text

    response_json = json.loads(response)

    # Iterate over the json file and make a list with binary markets with decimal odds

    decoded_events = []

    # Go through the the different markets in one event and find those that match to check get_market() performance
    for event in response_json:
        for market in decoded_markets:
            if market['id'] == event['id']:
                print(event.get('slug'))
                print(market.get('slug'))
            else:
                print('cry')

if __name__ == '__main__':
    main()