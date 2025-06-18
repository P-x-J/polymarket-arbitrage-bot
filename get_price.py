import requests
import json

url = "https://clob.polymarket.com/v1/orderbook?marketId=66&outcomeId=53533658763927947576373388517988930480829837993713096953177814292716552867756"
response = requests.request("GET", url)

print(response.text)