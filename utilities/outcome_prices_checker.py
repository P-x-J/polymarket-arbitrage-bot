import logging

log7 = logging.getLogger(__name__)

class OutcomePricesChecker:

    def __init__(self, outcome_prices: list[int]):
        self.outcome_prices = outcome_prices


    def count_outcome_prices(self) -> bool:
        # A two-outcome-markets list is expected per market
        if len(self.outcome_prices) == 2:
            log7.debug("outcome_prices is a two-elements list")
            return True
        else:
            log7.debug("outcome_prices isn't a two-element list")
            return False
