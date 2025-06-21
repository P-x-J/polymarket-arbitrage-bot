import requests
import json



def get_events():
    # Export active markets in polymarkets data
    url = "https://gamma-api.polymarket.com/events"

    # Use querystrings to list the market with various filtering and sorting options.

    response = requests.request("GET", url)

    response = response.text

    response_json = json.loads(response)

    # Iterate over the json file and make a list with binary markets with decimal odds

    decoded_events = []

    for event in response_json:
        if int(event['id']) == id:
            try:
                tags = event.get("tags")
                if outcome_price == None:
                    pass
            except AttributeError:
                # Only add the events that have outcomeprices listed
                pass
            else:
                id = event.get("id")
                slug = event.get("slug")
                decoded_events.append({"id": id, "tags": tags, "slug": slug})
        else:
            pass
        return decoded_events
