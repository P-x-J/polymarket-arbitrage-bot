import requests
import json


def get_markets():
    # Export active markets in polymarkets data
    url = "https://gamma-api.polymarket.com/markets"

    # Use querystrings to list the market with various filtering and sorting options.
    querystring = {"active":"true", "closed":"false"}

    response = requests.request("GET", url, params=querystring)

    response = response.text

    response_json = json.loads(response)

    # Iterate over the json file and make a list with binary markets with decimal odds

    decoded_events = []

    for event in response_json:
        try:
            outcome_price = event.get("outcomePrices")
            if outcome_price == None:
                pass
        except AttributeError:
            # Only add the events that have outcomeprices listed
            pass
        else:
            id = event.get("id")
            slug = event.get("slug")
            decoded_events.append({"id": id, "outcomePrices": outcome_price, "slug": slug})

    return decoded_events