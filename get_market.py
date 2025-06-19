import requests

# Export active markets in polymarkets data
url = "https://gamma-api.polymarket.com/markets"

querystring = {"active":"true", "closed":"false"}

response = requests.request("GET", url, params=querystring)

events = response.text

# Parse the data to a json file:


# Iterate over the json file and make a list with binary markets with decimal odds

decoded_events = []

for event in events:
    try:
        outcome_price = event.get("outcomePrices")
    except AttributeError:
        # Only add the events that have outcomeprices listed
        pass
    else:
        id = event.get("id")
        decoded_events.append({"id": id, "outcomePrices": outcome_price})

# Return the outcomePrices and id values of a market 

print(decoded_events)