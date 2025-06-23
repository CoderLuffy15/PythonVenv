import requests

def getprice(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=inr"
    response = requests.get(url)

    if response.status_code==200:
        data = response.json()
        print(data)
        price = data[coin]['inr']
        print(f"The current price of {coin.upper()} is ₹{price}")
    else:
        print("Failed to fetch price.")

coin = input("Enter Coin name: ")
getprice(coin)