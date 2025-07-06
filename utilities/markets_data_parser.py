import logging
import json
import requests
import re


log1 = logging.getLogger(__name__)

class MarketsDataParser:

    # Use querystrings to list the market with various filtering and sorting options
    querystrings = {
        "active":"true",
        "closed":"false"
        }
    # Create a class that extracts that from active markets
    def __init__(self, single_markets_gamma_api_url: str):
        self.single_markets_gamma_api_url = single_markets_gamma_api_url 
   
    
    def get_markets(self) -> list[dict[str, list[int]]]:
        # Export active markets in polymarkets data.
        response = requests.request("GET", self.single_markets_gamma_api_url, params=self.querystrings)
        response = response.text
        response_json = json.loads(response)

        decoded_markets = []

        # Iterate over the json file and make a list with binary markets with decimal odds

        for market in response_json:
            outcome_prices = market.get("outcomePrices")
            outcome_prices_str = str(outcome_prices)
            match = re.search(r'\[\"([0-9]+\.[0-9]+)\", \"([0-9]+\.[0-9]+)\"\]', outcome_prices_str.strip())
            
            if match:
                log1.debug("Found outcomePrices")
                outcome_prices = [float(match.group(1)), float(match.group(2))]


                id = market.get("id")
                slug = market.get("slug")
                decoded_markets.append({"id": id, "outcomePrices": outcome_prices, "slug": slug})
                log1.info("Append market to decoded_markets")
            else:
                log1.debug("Didn't find outcomePrices")
                pass

        return decoded_markets