import logging

log5 = logging.getLogger(__name__)

class ProbabilityCalculator():
    def __init__(self, outcome_odds_decimals: list[float]):
        self.outcome_odds_decimals = outcome_odds_decimals

    def calculate_probability(self) -> float:
        decimals = [(1/decimal)*100 for decimal in self.outcome_odds_decimals]
        return sum(decimals)
            