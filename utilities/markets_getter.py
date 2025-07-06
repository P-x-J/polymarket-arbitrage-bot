# Creates and refreshes all active markets inside a list
import logging
from multi_markets_data_parser import MultiMarketsDataParser
from markets_data_parser import MarketsDataParser

log8 = logging.getLogger(__name__)

class MarketsGetter(MultiMarketsDataParser):
	pass