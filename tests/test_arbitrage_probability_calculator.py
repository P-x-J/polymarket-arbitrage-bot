import pytest
from utilities.arbitrage_probability_calculator import ProbabilityCalculator

def test_calculate_probability():
    # Arbitrage opportunitie

    test1 = ProbabilityCalculator([2.10, 2.10])
    assert test1.calculate_probability() == 95.24

    test2 = ProbabilityCalculator([1.95, 2.10])
    assert test2.calculate_probability() == 98.90

    test3 = ProbabilityCalculator([2.05, 2.05])
    assert test3.calculate_probability() == 97.56

    # Non-arbitrage cases

    test4 = ProbabilityCalculator([1.80, 2.10])
    assert test4.calculate_probability() == 103.18

    test5 = ProbabilityCalculator([1.70, 2.40])
    assert test5.calculate_probability() == 100.49
