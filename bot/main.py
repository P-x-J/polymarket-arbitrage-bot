import json
import logging
import requests
import re
import sys
import time



from utils import ArbitrageDetector
from utils import DecimalOddsSetter
from utils import get_api
from utils import MarketsDataParser
from utils import MultiMarketsDataParser
from utils import OutcomePricesChecker
from utils import ProbabilityCalculator
from utils import PolymarketMarketsSetter
from utils import set_minimum_price_gap


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def main():
    minimum_price_gap = set_minimum_price_gap()
    single_markets_data_parser = MarketsDataParser("https://gamma-api.polymarket.com/markets")
    events_data_parser = MultiMarketsDataParser("https://gamma-api.polymarket.com/events")

    while True:
        try:
            decoded_markets = single_markets_data_parser.get_markets()
            decoded_events_markets = events_data_parser.get_events()

            for market in decoded_markets:
                outcome_prices = decoded_events_markets.get("OutcomePrices")
                outcome_prices_checker = OutcomePricesChecker(outcome_prices)

                if outcome_prices_checker.check_outcome_prices and outcome_prices_checker.count_outcome_prices:

                    decimal_odds_setter = DecimalOddsSetter(outcome_prices)
                    outcome_odds_decimals = decimal_odds_setter.convert_to_decimal()
                    
                    probability_calculator = ProbabilityCalculator(outcome_odds_decimals)
                    arbitrage_probability = probability_calculator.calculate_probability()

                    arbitrage_detector = ArbitrageDetector(arbitrage_probability, minimum_price_gap)

                else:
                    pass


        except KeyboardInterrupt:
            break   

        else:
            break

if __name__ == '__main__':
    main()