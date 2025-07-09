from utils.arbitrage_detector import ArbitrageDetector
from utils.decimal_odds_setter import DecimalOddsSetter
from utils.get_api import get_api
from utils.markets_data_parser import MarketsDataParser
from utils.multi_markets_data_parser import MultiMarketsDataParser
from utils.outcome_prices_checker import OutcomePricesChecker
from utils.arbitrage_probability_calculator import ProbabilityCalculator
from utils.markets_getter import PolymarketMarketsSetter
from utils.set_minimum_price_gap import set_minimum_price_gap

import requests
import re
import logging
import json
import time


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