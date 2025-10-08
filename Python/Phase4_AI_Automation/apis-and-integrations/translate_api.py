import requests

def translate_text(text, target_lang="en"):
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=auto|{target_lang}"
    response = requests.get(url).json()
    translation = response['responseData']['translatedText']
    return translation

if __name__ == "__main__":
    text = input("Enter text to translate: ")
    target = input("Target language code (e.g., en, es, fr): ")
    print("Translation:", translate_text(text, target))
