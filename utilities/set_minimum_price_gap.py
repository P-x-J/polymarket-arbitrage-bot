import logging


log3 = logging.getLogger(__name__)


def set_minimum_price_gap() -> float:
    # A minimum of 1.5 is recommended
    logging.info('Requested user to set a minimum price gap number')
    while True:
        try:
            minimum_price_gap = input('Set minimum price gap number: ')
            minimum_price_gap = float(minimum_price_gap)
            if minimum_price_gap <= 0:
                raise ValueError
        except ValueError:
            logging.error("The minimum price gap must be a float")
            pass
        else:
            return minimum_price_gap
    