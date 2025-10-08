import requests

def get_crypto_price(coin="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url).json()

    if coin not in response:
        print("❌ Coin not found")
        return

    price = response[coin]["usd"]
    print(f"Current price of {coin}: ${price}")

if __name__ == "__main__":
    coin_name = input("Enter coin (e.g., bitcoin, ethereum): ").lower()
    get_crypto_price(coin_name)
