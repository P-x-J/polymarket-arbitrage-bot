import pytest
from utilities.arbitrage_detector import ArbitrageDetector

def test_detect_abitrage_opportunity():
    test1 = ArbitrageDetector(98.499999999, 1.5)
    assert test1.detect_arbitrage_opportunity == True

    test2 = ArbitrageDetector(97.3, 1.5)
    assert test2.detect_arbitrage_opportunity == True

    test3 = ArbitrageDetector(99, 1.5)
    assert test3.detect_arbitrage_opportunity == False

    test4 = ArbitrageDetector(100.000134, 0)
    assert test4.detect_arbitrage_opportunity == False