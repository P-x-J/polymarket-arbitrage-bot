# Creates and refreshes all active markets inside a list
import logging
from multi_markets_data_parser import MultiMarketsDataParser
from markets_data_parser import MarketsDataParser

log8 = logging.getLogger(__name__)

class PolymarketMarketsSetter(MultiMarketsDataParser, MarketsDataParser):

	def __init__(self, event_gamma_api_url: str, single_markets_gamma_api_url: str):
		MultiMarketsDataParser.__init__(self, event_gamma_api_url)
		MarketsDataParser.__init__(self, single_markets_gamma_api_url)


	def extract_markets(self):
		single_markets = self.get_markets()
		return single_markets

	def extract_events_markets(self):
		events = self.get_events()
		multi_markets = []

		for event_markets in events:
			event_multi_markets = event_markets["markets"]

			for multi_market in event_multi_markets:
				multi_markets.append(multi_market)

		return multi_markets
	
	def unify_markets_lists(self, single_markets: list[dict], multi_markets: list[dict]) -> list[dict]:
		# Make dictionnaries hashable befefore uniting the lists

		single_markets = single_markets or []
		multi_markets = multi_markets or []

		seen_ids = set()
		polymarket_active_markets = []

		for market in single_markets + multi_markets:
			market_id = market.get("id")  # Use 'slug' or another unique key if needed
			if market_id and market_id not in seen_ids:
				seen_ids.add(market_id)
				polymarket_active_markets.append(market)

		return polymarket_active_markets


# Example usage:
#
# getter = PolymarketMarketsSetter("https://gamma-api.polymarket.com/events",
#					    "https://gamma-api.polymarket.com/markets")
# single_markets = getter.extract_markets()
# multi_markets = getter.extract_events_markets()
# polymarket_markets = getter.unify_markets_lists(single_markets, multi_markets)
