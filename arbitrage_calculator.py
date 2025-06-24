import requests
import re
import logging
import json


logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
# Build a function that takes operation's values and determines whether there's an arbitrage opportunity withing these values.
# Identify binary arbitrage operation's variables 


def main():
    single_markets_data = MarketsData("https://gamma-api.polymarket.com/markets")
    single_decoded_markets = single_markets_data.get_markets()
    # Create a for loop that goes through every market active in Polymarket 

    # makes sure it's a binary market

    # converts the outcomes prices (odds) into the decimal odds numbers
    
    # Determine whether there' an arbitrage opportunity
    # If there's an arbitrage opportunity it sends a notification via """ including the profit percentage and market's details
    # If there's no arbitrage opportunity it just keeps running 
    # The bot won't stop until the user manually stops it by pressing CTRL+C


class MarketsData():
    querystring = {"active":"true", "closed":"false"}
    # Create a class that extracts that from active markets
    def __init__(self, gamma_api_data_url: str):
        self.gamma_api_data_url = gamma_api_data_url
    
    def get_markets(self) -> list[dict[str]]:
        # Export active markets in polymarkets data

        # Use querystrings to list the market with various filtering and sorting options.
        response = requests.request("GET", self.gamma_api_data_url, params=self.querystring)
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
    

    def get_events(self) -> list[dict[str, any]]:
        response = requests.request("GET", self.gamma_api_data_url, params=self.querystring)
        response = response.text
        response_json = json.loads(response)

        decoded_event_markets = []

        for event in response_json:
            # get the list of multi-markets events of the recent events
            if len(event["markets"])>= 1:

                id = event.get("id")
                event_slug = event.get("slug")
                for tag in event.get("tags"):
                    tid = tag.get("id")

                decoded_event_markets.append({"id": id, "tid": tid, "slug": slug, "markets": []})

                for market in event.get("markets"):
                    outcome_price = market.get("outcomePrices")
                    match = re.search(r"[\"]")
                    
                        pass
                    else:
                        id = market.get("id")
                        slug = market.get("slug")
                        markets = decoded_event_markets["markets"]
                        markets.append({"id": id, "outcomePrices": outcome_price, "slug": slug})
            else:
                pass
        return decoded_event_markets

            
                    

class Probabilities():
    """
    Manage the prices from the market's outcomes and determine whether an arbitrage opportunity exists
    """
    def __init__(self, outcome_prices: str):
        self.outcome_prices = outcome_prices

    
    def get_outcomes(self, outcome_prices) -> tuple[int, int]:
        """Use regular expressions to extract the outcome prices from an string"""


    def calc_arb_percent(self, outcome_A_decimal, outcome_B_decimal) -> tuple[bool, str]:
        """Determines whether an arbitrage opportunity exists"""

        # Expects the decimal percentage of the two possible outcomes.
        try: 
            outcome_A_decimal = float(outcome_A_decimal)
            outcome_B_decimal = float(outcome_B_decimal)
        except ValueError:
            return False, "Invalid input: outcomes must be decimal numbers"
    

        # Calculate implied probabilities
        player_A_prob = (1/outcome_A_decimal)*100
        player_B_prob = (1/outcome_B_decimal)*100
        total_prob = player_A_prob + player_B_prob


        # If total_prob < 100% then there's an arbitrage opportunity
        if total_prob < 100:
            profit = 100 - total_prob
            return True, f"+{profit:.2f}% arbitrage profit"
        else:
            loss = total_prob - 100
            return True, f"-{loss:.2f} inefficiency"
        


    def price_to_dec_odds(self, price_numbers) -> list[int]:
        """Outputs the decimal odd number of the inputted outcome price"""
        decimal_odds_numbers = []

        for price in price_numbers:
            decimal_odd_number = 1/int(price)
            decimal_odds_numbers.append(decimal_odd_number)
    
        # Supposed to return a two-elements list as it's a binary market, Test with len(decimal_odds_numbers) = 2
        return decimal_odds_numbers
        