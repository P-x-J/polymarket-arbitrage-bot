import sys
import requests
import webbrowser
import logging


logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w"
                    format="%(acstime)s - %(levelname)s - %(message)s")

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
    
    def get_markets(self) -> list:
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
    

    def get_events(self) -> list:
        response = requests.request("GET", self.gamma_api_data_url, params=self.querystring)
        response = response.text
        response_json = json.loads(response)

        decoded_market = []

        for event in response_json:
            # get the list of multi-markets events of the recent events




def calc_arb_percent(outcome_A_decimal, outcome_B_decimal):
    """Determines whether an arbitrage opportunity exists"""
    #Expects the decimal percentage of the two possible outcomes.
    try: 
        float(outcome_A_decimal, outcome_B_decimal)
    except ValueError:
        sys.exit("Outcome A & B weren't given as decimal numbers")
    else:
        # Player A wins
        player_A_wins = (1/outcome_A_decimal)x 100
        player_B_wins = (1/outcome_B_decimal)x 100
        total_prob = player_A_wins + player_B_wins
        # If total_prob < 100% then there's an arbitrage opportunity
        if total_prob < 100:
            # Returns true if there's an arbitrage opportunity and profit percentage
            return True, str("+", float(100-total_prob) + "%")
        elif total_prob >= 100:
            # returns false if there's no arbitrage opportunity and losing percentage
            return True, str("-", float(-(100-total_prob)) + "%")
        


def price_to_dec_odds(price_numbers):
    """Outputs the decimal odd number of the inputted outcome price"""
    decimal_odds_numbers = []

    for price in price_numbers:
        decimal_odd_number = 1/int(price)
        decimal_odds_numbers.append(decimal_odd_number)
    
    # Supposed to return a two-elements list as it's a binary market, Test with len(decimal_odds_numbers) = 2
    return decimal_odds_numbers
        