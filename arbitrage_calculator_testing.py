import requests
import re
import logging
import json
import time


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


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