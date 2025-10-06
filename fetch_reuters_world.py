# fetch_reuters_world.py
import requests
from datetime import datetime

def fetch_page():
    url = "https://www.reuters.com/world/"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)

    # Add a timestamp at the top for visibility
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    html = f"<!-- Last updated: {timestamp} -->\n" + r.text

    # Save as index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Saved latest Reuters World snapshot ({timestamp})")

if __name__ == "__main__":
    fetch_page()
