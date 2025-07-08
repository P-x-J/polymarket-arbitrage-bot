import pytest
from unittest.mock import patch
from utilities.set_minimum_price_gap import set_minimum_price_gap

def test_set_minimum_price_gap():
    with patch('builtins.input', return_value='1.8'):
        assert set_minimum_price_gap() == 1.8

    with patch('builtins.input', return_value='hello'):
        with set_minimum_price_gap():
            pytest.raises(ValueError)





