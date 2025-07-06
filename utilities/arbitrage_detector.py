import logging

log6 = logging.getLogger(__name__)

class ArbitrageDetector:
    def __init__(self, probability: float, minimum_price_gap: float):
        self.minimum_price_gap = minimum_price_gap
        self.probability = probability

    def detect_arbitrage_opportunity(self) -> tuple[bool, str]:
        """Determines whether an arbitrage opportunity exists"""

        if self.probability < 100 - self.minimum_price_gap:
            log6.info(f"{self.probability:.2f}% arbitrage percentage")
            return True, f"{self.probability:.2f}% arbitrage percentage"

        else:
            log6.info(f"No arbitrage opportunity: {self.probability:.2f}")
            return True, f"No arbitrage opportunity: {self.probability:.2f}%"
            
