import requests
import json



def get_events():
    # Export active markets in polymarkets data
    url = "https://gamma-api.polymarket.com/events"

    # Use querystrings to list the market with various filtering and sorting options.
    querystring = {"active":"True", "closed":"False"}
    response = requests.request("GET", url, params=querystring)
    print(type(response))
    response = response.text
    print(type(response))

    response_json = json.loads(response)
    print(type(response_json))

    # Iterate over the json file and make a list with binary markets with decimal odds

    decoded_events = []



get_events()