import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")
    for q in quotes:
        text = q.find("span", class_="text").get_text()
        author = q.find("small", class_="author").get_text()
        print(f"{text} — {author}")

if __name__ == "__main__":
    scrape_quotes()
