import pyautogui
import time
import os

def auto_screenshot(interval=5, count=3, folder="screenshots"):
    os.makedirs(folder, exist_ok=True)
    for i in range(count):
        filename = os.path.join(folder, f"screenshot_{i+1}.png")
        pyautogui.screenshot(filename)
        print(f"📸 Saved {filename}")
        time.sleep(interval)

if __name__ == "__main__":
    auto_screenshot()
