import requests

url = "https://clob.polymarket.com/book"

querystring = {"token_id":"53135072462907880191400140706440867753044989936304433583131786753949599718775"}

response = requests.request("GET", url, params=querystring)

print(response.text)