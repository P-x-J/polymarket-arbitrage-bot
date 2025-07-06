import logging
import json
import requests
import re


log2 = logging.getLogger(__name__)

class MultiMarketsDataParser:

    querystrings = {
        "active":"true",
        "closed":"false"
        }
    
    def __init__(self, event_gamma_api_url: str):
        self.event_gamma_api_url = event_gamma_api_url

    def get_events(self) -> list[dict[str, any]]:
        response = requests.request("GET", self.event_gamma_api_url, params=self.querystrings)
        response = response.text
        response_json = json.loads(response)

        for event in response_json:
            # get the list of multi-markets events of the recent events
            if len(event["markets"])>= 1:
                log2.debug("Found an event with at least 1 market")

                event_id = event.get("id")
                event_slug = event.get("slug")
                tags = event.get("tags")
                for tag in tags:
                    event_tid = tag.get("id")

                decoded_events_markets = []
                multi_markets = []

                for market in event.get("markets"):    

                    outcome_prices = market.get("outcomePrices")
                    outcome_prices_str = str(outcome_prices)

                    # The outcomePrices musst be given as a formatted string of two elements, if not pass
                    match = re.search(r'\[\"([0-9]+\.[0-9]+)\", \"([0-9]+\.[0-9]+)\"\]', outcome_prices_str)

                    if match:
                        log2.debug("Found outcomePrices")
                        outcome_prices = [float(match.group(1)), float(match.group(2))]
                        

                        market_id = market.get("id")
                        slug = market.get("slug")
                        # Make a list of markets inside the events dictionnary

                        multi_markets.append({"id": market_id, "outcomePrices": outcome_prices, "slug": slug})
                    else: 
                        log2.debug("Didn't find outcomePrices")
                        pass
                decoded_events_markets.append({"id": event_id, "tid": event_tid, "slug": event_slug, "markets": multi_markets})
            
            else:
                log2.debug("Event with no markets")
                pass

        return decoded_events_markets
