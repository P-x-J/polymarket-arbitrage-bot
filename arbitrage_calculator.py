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
    
    def get_markets(self) -> list[dict[str, list[int]]]:
        # Export active markets in polymarkets data

        # Use querystrings to list the market with various filtering and sorting options.
        response = requests.request("GET", self.gamma_api_data_url, params=self.querystring)
        response = response.text
        response_json = json.loads(response)

        # Iterate over the json file and make a list with binary markets with decimal odds

        decoded_markets = []
 
        for market in response_json:
            outcome_prices_str = market.get("outcomePrices")
            match = re.search(r'\[\"([0-9.]+)\", \"([0-9]+)\"\]', outcome_prices_str)
            
            if match:
                logging.debug("Found outcomePrices")
                outcome_prices = []
                outcome_price1 = float(match.group(1))
                outcome_price2 = float(match.group(2))
                outcome_prices.append(outcome_price1)
                outcome_prices.append(outcome_price2)


                id = market.get("id")
                slug = market.get("slug")
                decoded_markets.append({"id": id, "outcomePrices": outcome_prices, "slug": slug})
                logging.info("Append market to decoded_markets")
            else:
                logging.debug("Didn't find outcomePrices")
                pass

        return decoded_markets
    

    def get_events(self) -> list[dict[str, any]]:
        response = requests.request("GET", self.gamma_api_data_url, params=self.querystring)
        response = response.text
        response_json = json.loads(response)

        decoded_event_markets = []

        for event in response_json:
            # get the list of multi-markets events of the recent events
            if len(event["markets"])>= 1:
                logging.debug("Found an event with at least 1 market")

                id = event.get("id")
                event_slug = event.get("slug")
                for tag in event.get("tags"):
                    tid = tag.get("id")

                decoded_event_markets.append({"id": id, "tid": tid, "slug": slug, "markets": []})

                for market in event.get("markets"):
                    outcome_prices_str = market.get("outcomePrices")
                    # The outcomePrices musst be given as a formatted string of two elements, if not pass
                    match = re.search(r'\[\"([0-9.]+)\", \"([0-9]+)\"\]', outcome_prices_str)


                    if match:
                        logging.debug("Found outcomePrices")
                        outcome_prices = []
                        outcome_price1 = float(match.group(1))
                        outcome_price2 = float(match.group(2))
                        outcome_prices.append(outcome_price1)
                        outcome_prices.append(outcome_price2)
                        

                        id = market.get("id")
                        slug = market.get("slug")
                        # Make a list of markets inside the events dictionnary
                        decoded_event_markets["markets"].append({"id": id, "outcomePrices": outcome_prices, "slug": slug})
                    else: 
                        logging.debug("Didn't find outcomePrices")
                        pass
            
            else:
                logging.debug("Event with no markets")
                pass

        return decoded_event_markets

            
                    

class Probabilities():
    """
    Manage the prices from the market's outcomes and determine whether an arbitrage opportunity exists
    """
    def __init__(self, outcome_prices: list[int]):
        self.outcome_prices = outcome_prices

    def check_outcome_prices(self) -> bool:
        """Check that there are only two prices"""
        if len(self.outcome_prices) == 2:
            logging.debug("outcome_prices is a two-elements list")
            return True
        else:
            logging.debug("outcome_prices isn't a two-element list")
            return False


    def calc_arb_percent(self) -> tuple[bool, str]:
        """Determines whether an arbitrage opportunity exists"""

        # Expects the decimal percentage of the two possible outcomes.
        try: 
            outcome_A_decimal = float(self.outcome_prices[0])
            outcome_B_decimal = float(self.outcome_prices[1])
        except ValueError:
            logging.debug("The outcomes A & B aren't given as floats")
            return False, "Invalid input: outcomes must be decimal numbers"

    

        # Calculate implied probabilities
        player_A_prob = (1/outcome_A_decimal)*100
        player_B_prob = (1/outcome_B_decimal)*100
        total_prob = player_A_prob + player_B_prob
        logging.info("Calculated the implied probabilities")


        # If total_prob < 100% then there's an arbitrage opportunity
        if total_prob < 100:
            profit = 100 - total_prob
            logging.info(f"We're winning +{profit:.2f}")
            return True, f"+{profit:.2f}% arbitrage profit"

        else:
            loss = total_prob - 100
            logging.info(f"We're lossing -{loss:.2f}")
            return True, f"-{loss:.2f} inefficiency"
            



    def price_to_dec_odds(self, price_numbers: list[float]) -> list[int]:
        """Outputs the decimal odd number of the inputted outcome price"""
        decimal_odds_numbers = []

        for price in price_numbers:
            decimal_odd_number = 1/float(price)
            decimal_odds_numbers.append(decimal_odd_number)
        logging.info("Returned decimal odd numbers")
    
        # Supposed to return a two-elements list as it's a binary market, Test with len(decimal_odds_numbers) = 2
        return decimal_odds_numbers
        