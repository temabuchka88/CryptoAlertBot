import requests
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("API_KEY")
def get_coin_price(coin_symbol):
    api_key = key
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={coin_symbol}&convert=USD'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        price = data['data'][coin_symbol]['quote']['USD']['price']
        return price
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
