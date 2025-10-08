import feedparser

def get_headlines():
    rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)

    print("🗞️ Latest News Headlines:\n")
    for entry in feed.entries[:10]:
        print("-", entry.title)

if __name__ == "__main__":
    get_headlines()
