import logging

log4 = logging.getLogger(__name__)

class DecimalOddsSetter:
    """
    Manage the prices from the market's outcomes and determine whether an arbitrage opportunity exists
    """

    def __init__(self, outcome_prices: list[int]):
        self.outcome_prices = outcome_prices


    def count_outcome_prices(self) -> bool:
        """Check that there are only two prices"""
        if len(self.outcome_prices) == 2:
            log4.debug("outcome_prices is a two-elements list")
            return True
        else:
            log4.debug("outcome_prices isn't a two-element list")
            return False


    def convert_to_decimal(self) -> list[float]:
        """Outputs the decimal odd number of the inputted outcome price"""
        decimal_odds_numbers = []

        for price in self.outcome_prices:
            decimal_odd_number = 1/float(price)
            decimal_odds_numbers.append(float(decimal_odd_number))
        log4.info("Returned decimal odd numbers")
    
        # Supposed to return a two-elements list as it's a binary market, Test with len(decimal_odds_numbers) = 2
        return decimal_odds_numbers
    
    def check_decimal_odds(self) -> bool: 
        pass