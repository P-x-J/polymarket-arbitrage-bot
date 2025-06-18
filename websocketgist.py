import websocket
import json
import threading
import time
import csv
import logging
import requests


def on_open(ws):
    listOfTokens = [] #put the token ID's here
    subscribe_message = {
        "type": "Market",
        "assets_ids": listOfTokens[:1]
    }
    ws.send(json.dumps(subscribe_message))
    logging.info("Sent subscribe message\n")
    
    def run(*args):
        while True:
            time.sleep(30)
            ws.send(json.dumps({"type": "ping"}))
            logging.info("Ping!\n")
    
    threading.Thread(target=run).start()

    
    def on_message(ws, message):
        try:
            converted_message = json.loads(message)
        except json.JSONDecodeError:
            logging.info(f"Received non-JSON message: {message}")
            return

    event_type = converted_message.get('event_type', 'Unknown')
    if event_type == 'book':
         logging.info(f"Book: {message}")
        # handle_book_message(converted_message)
    elif event_type == 'price_change':
        # handle_price_change_message(converted_message)
         logging.info(f"Price Change: {message}")
         
    elif event_type == 'last_trade_price':
         logging.info(f"last trade price: {message}")
         
        # handle_last_trade_price_message(converted_message)
    else:
        logging.info(f"Received unknown message type: {event_type}")
        logging.info(json.dumps(converted_message, indent=4))
    logging.info("\n" + "_"*50 + "\n")

def handle_book_message(message):
    logging.info("Book Message Received")
    asset_id = message.get('asset_id', 'Unknown')
    market = message.get('market', 'Unknown')
    neg_risk = neg_risk_status.get(asset_id, False)
    market_title = dictOfTitles.get(asset_id, "Unknown Market Title")
    outcome = outcome_context.get(asset_id, "Unknown Outcome")
    logging.info(f"Market Title: {market_title}")
    logging.info(f"Outcome: {outcome}")
    logging.info(f"Asset ID: {asset_id}")
    logging.info(f"Market: {market}")
    logging.info(f"Neg Risk: {neg_risk}")
    logging.info("Buys (Bids):")
    bids = message.get('bids', [])
    if not bids:
        logging.info("  No buy orders")
    for bid in bids:
        logging.info(f"  Price: {bid['price']}, Size: {bid['size']}")
    logging.info("Sells (Asks):")
    asks = message.get('asks', [])
    if not asks:
        logging.info("  No sell orders")
    for ask in asks:
        logging.info(f"  Price: {ask['price']}, Size: {ask['size']}")

def handle_price_change_message(message):
    logging.info("Price Change Message Received")
    asset_id = message.get('asset_id', 'Unknown')
    market = message.get('market', 'Unknown')
    price = message.get('price', 'Unknown')
    size = message.get('size', 'Unknown')
    side = message.get('side', 'Unknown')
    time = message.get('time', 'Unknown')
    neg_risk = neg_risk_status.get(asset_id, False)
    market_title = dictOfTitles.get(asset_id, "Unknown Market Title")
    outcome = outcome_context.get(asset_id, "Unknown Outcome")
    logging.info(f"Market Title: {market_title}")
    logging.info(f"Outcome: {outcome}")
    logging.info(f"Asset ID: {asset_id}")
    logging.info(f"Market: {market}")
    logging.info(f"Neg Risk: {neg_risk}")
    logging.info(f"Price: {price}")
    logging.info(f"Size: {size}")
    logging.info(f"Side: {side}")
    logging.info(f"Time: {time}")

def handle_last_trade_price_message(message):
    logging.info("Last Trade Price Message Received")
    asset_id = message.get('asset_id', 'Unknown')
    market = message.get('market', 'Unknown')
    fee_rate_bps = message.get('fee_rate_bps', 'Unknown')
    price = message.get('price', 'Unknown')
    side = message.get('side', 'Unknown')
    size = message.get('size', 'Unknown')
    timestamp = message.get('timestamp', 'Unknown')
    neg_risk = neg_risk_status.get(asset_id, False)
    market_title = dictOfTitles.get(asset_id, "Unknown Market Title")
    outcome = outcome_context.get(asset_id, "Unknown Outcome")
    logging.info(f"Market Title: {market_title}")
    logging.info(f"Outcome: {outcome}")
    logging.info(f"Asset ID: {asset_id}")
    logging.info(f"Market: {market}")
    logging.info(f"Neg Risk: {neg_risk}")
    logging.info(f"Fee Rate BPS: {fee_rate_bps}")
    logging.info(f"Price: {price}")
    logging.info(f"Side: {side}")
    logging.info(f"Size: {size}")
    logging.info(f"Timestamp: {timestamp}")

def on_error(ws, error):
    logging.info("Error: ", error)

def on_close(ws, close_status_code, close_msg):
    logging.info("Connection closed")

if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws-subscriptions-clob.polymarket.com/ws/market",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(ping_interval=30, ping_timeout=10)