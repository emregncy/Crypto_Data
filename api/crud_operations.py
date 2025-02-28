import json
from utils.file_handler import read_from_file, save_to_file

DATA_FILE = "crypto_data.json"

def save_data(data):

    save_to_file(data, DATA_FILE)

def get_cryptos():

    return read_from_file(DATA_FILE)

def update_price(crypto_name, new_price):

    data = read_from_file(DATA_FILE)
    for coin in data:
        if coin["name"].lower() == crypto_name.lower():
            coin["current_price"] = new_price
            save_to_file(data, DATA_FILE)
            return f"{crypto_name} fiyatı güncellendi."
    return f"{crypto_name} bulunamadı."

def delete(crypto_name):
    data = read_from_file(DATA_FILE)
    new_data = [coin for coin in data if coin["name"].lower() != crypto_name.lower()]
    
    if len(new_data) == len(data):
        return f"{crypto_name} bulunamadı."
    
    save_to_file(new_data, DATA_FILE)
    return f"{crypto_name} silindi."
