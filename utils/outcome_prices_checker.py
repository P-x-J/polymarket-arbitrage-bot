import logging

log7 = logging.getLogger(__name__)

class OutcomePricesChecker:

    def __init__(self, outcome_prices: list[float]):
        self.outcome_prices = outcome_prices


    def count_outcome_prices(self) -> bool:
        # A two-outcome-markets list is expected per market
        if len(self.outcome_prices) == 2:
            log7.debug("outcome_prices is a two-elements list")
            return True
        else:
            log7.debug("outcome_prices isn't a two-element list")
            return False
    
    def check_outcome_prices(self) -> bool:
        try: 
            for outcome_price in self.outcome_prices:
                outcome_price = float(outcome_price)
                # The decimal number
        except ValueError:
            log7.debug("Outcome prices aren't given as float numbers")
            return False
        else:
            return True
