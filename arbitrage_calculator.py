import requests
import re
import logging
import json
import time


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    single_markets_data = MarketsData("https://gamma-api.polymarket.com/markets")
    events_data = MarketsData("https://gamma-api.polymarket.com/events")
    
    while True:
        try:
            single_decoded_markets = single_markets_data.get_markets()
            events_decoded = events_data.get_events()

            for market in single_decoded_markets:
                outcome_prices = market["outcomePrices"]
                prob = Probabilities(outcome_prices)
                if prob.check_outcome_prices():
                    decimal_odds = prob.price_to_dec_odds()
                    opportunity, percentage = prob.calc_arb_percent(decimal_odds)
                    if opportunity == True:
                        print(percentage + f"in single market id = {market["id"]}")
                    else:
                        pass
            
                else:
                    pass
            

            for event in events_decoded:
                markets = event["markets"]
                for market in markets:
                    outcome_prices = market["outcomePrices"]
                    prob = Probabilities(outcome_prices)
                    if prob.check_outcome_prices():
                        decimal_odds = prob.price_to_dec_odds()
                        print(f"decimal odds: {decimal_odds}")
                        opportunity, percentage = prob.calc_arb_percent(decimal_odds)

                        if opportunity == True:
                            print(percentage + f"in single market id = {market["id"]} in event {event["tid"], event["slug"]}")
                        else:
                            pass


                    else:
                        pass
        except KeyboardInterrupt:
            logging.debug("Pressed CTRL+C")
            break

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
            outcome_prices = market.get("outcomePrices")
            outcome_prices_str = str(outcome_prices)
            match = re.search(r'\[\"([0-9]+\.[0-9]+)\", \"([0-9]+\.[0-9]+)\"\]', outcome_prices_str.strip())
            
            if match:
                logging.debug("Found outcomePrices")
                outcome_prices = [float(match.group(1)), float(match.group(2))]


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

                event_id = event.get("id")
                event_slug = event.get("slug")
                tags = event.get("tags")
                for tag in tags:
                    event_tid = tag.get("id")


                multi_markets = []

                for market in event.get("markets"):    

                    outcome_prices = market.get("outcomePrices")
                    outcome_prices_str = str(outcome_prices)

                    # The outcomePrices musst be given as a formatted string of two elements, if not pass
                    match = re.search(r'\[\"([0-9]+\.[0-9]+)\", \"([0-9]+\.[0-9]+)\"\]', outcome_prices_str)


                    if match:
                        logging.debug("Found outcomePrices")
                        outcome_prices = [float(match.group(1)), float(match.group(2))]
                        

                        market_id = market.get("id")
                        slug = market.get("slug")
                        # Make a list of markets inside the events dictionnary

                        multi_markets.append({"id": market_id, "outcomePrices": outcome_prices, "slug": slug})
                    else: 
                        logging.debug("Didn't find outcomePrices")
                        pass
                decoded_event_markets.append({"id": event_id, "tid": event_tid, "slug": event_slug, "markets": multi_markets})
            
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

    def count_outcome_prices(self) -> bool:
        """Check that there are only two prices"""
        if len(self.outcome_prices) == 2:
            logging.debug("outcome_prices is a two-elements list")
            return True
        else:
            logging.debug("outcome_prices isn't a two-element list")
            return False


    def convert_to_decimal(self) -> list[float]:
        """Outputs the decimal odd number of the inputted outcome price"""
        decimal_odds_numbers = []

        for price in self.outcome_prices:
            decimal_odd_number = 1/float(price)
            decimal_odds_numbers.append(float(decimal_odd_number))
        logging.info("Returned decimal odd numbers")
    
        # Supposed to return a two-elements list as it's a binary market, Test with len(decimal_odds_numbers) = 2
        return decimal_odds_numbers
    

    def set_minimum_price_gap() -> float:
        minimum_price_gap = input('Set minimum price gap number: ')
        return float(minimum_price_gap)



    def calculate_probability(self, outcome_odds_decimals: list[float]) -> float:
        decimals = [(1/decimal)*100 for decimal in outcome_odds_decimals]
        return sum(decimals)
            
            

    def detect_arbitrage_opportunity(self, probability: float, minimum_price_gap: float) -> tuple[bool, str]:
        """Determines whether an arbitrage opportunity exists"""

        if probability < 100 - minimum_price_gap:
            logging.info(f"{probability:.2f}% arbitrage percentage")
            return True, f"{probability:.2f}% arbitrage percentage"

        else:
            logging.info(f"No arbitrage opportunity: {probability:.2f}")
            return True, f"No arbitrage opportunity: {probability:.2f}%"
            

        
if __name__ == '__main__':
    main()