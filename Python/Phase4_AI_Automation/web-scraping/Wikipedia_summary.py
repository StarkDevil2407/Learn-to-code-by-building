import requests

def wiki_summary(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        print("\n📘 Title:", data.get("title"))
        print("\n🧾 Summary:\n", data.get("extract"))
    else:
        print("❌ Could not fetch summary. Try another topic.")

if __name__ == "__main__":
    search = input("Enter topic: ")
    wiki_summary(search)
