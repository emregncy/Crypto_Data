from api.fetch_data import fetch_crypto_data
from api.crud_operations import save_data, get_cryptos, update_price, delete

def main():
    
    crypto_data = fetch_crypto_data(limit=5) 
    for coin in crypto_data:
        print(f"- {coin['name']} ({coin['symbol'].upper()}): ${coin['current_price']}")

    save_data(crypto_data)

    print(update_price("Bitcoin", 50000))

    print(delete("Ethereum"))

if __name__ == "__main__":
    main()
