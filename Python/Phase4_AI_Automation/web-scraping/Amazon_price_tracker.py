import requests
from bs4 import BeautifulSoup

def get_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.find("span", id="productTitle")
    price = soup.find("span", class_="a-price-whole")

    if title and price:
        print(f"Product: {title.text.strip()}")
        print(f"Price: ₹{price.text.strip()}")
    else:
        print("Could not find price info (page structure may have changed).")

if __name__ == "__main__":
    link = input("Enter Amazon product URL: ")
    get_price(link)
