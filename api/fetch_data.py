import requests

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

def fetch_crypto_data(currency="usd", limit=10):
    params = {
        "vs_currency": currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "API isteği başarısız", "status_code": response.status_code}
