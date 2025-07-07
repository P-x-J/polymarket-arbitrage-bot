from utilities.outcome_prices_checker import OutcomePricesChecker
import pytest

def test_count_outcome_prices():
    assert OutcomePricesChecker.count_outcome_prices([]) == False
    assert OutcomePricesChecker.count_outcome_prices([0.1234, 0.1234878]) == True

def test_check_outcome_prices():
    with pytest.raises(ValueError):
        OutcomePricesChecker.check_outcome_prices(["Hello", 0.12])

    assert OutcomePricesChecker.check_outcome_prices([0.1234, 0.2341])

