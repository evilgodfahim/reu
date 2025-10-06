# reuters_world_rss.py
import requests
from bs4 import BeautifulSoup
import datetime

def fetch_reuters_world():
    url = "https://www.reuters.com/world/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    selectors = [
        ".heading-module__base__p-zaD.heading-module__heading_6__-zrtS",
        ".heading-module__base__p-zaD.heading-module__heading_6_bold__795rd",
        ".heading-module__base__p-zaD.heading-module__heading_6_light__klgho",
        ".heading-module__base__p-zaD.heading-module__heading_6_rtl__00wC5",
        ".heading-module__base__p-zaD.heading-module__heading_6_small__B-tum"
    ]

    articles = []
    for selector in selectors:
        for tag in soup.select(selector):
            a = tag.find("a")
            if a and a["href"].startswith("/world"):
                title = a.get_text(strip=True)
                link = "https://www.reuters.com" + a["href"]
                articles.append((title, link))
    return articles


def generate_rss(articles):
    now = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>Reuters World (Unofficial)</title>
<link>https://www.reuters.com/world/</link>
<description>Automated Reuters World News feed (unofficial)</description>
<lastBuildDate>{now}</lastBuildDate>
"""
    for title, link in articles[:20]:
        rss += f"""
<item>
<title>{title}</title>
<link>{link}</link>
<guid>{link}</guid>
<pubDate>{now}</pubDate>
</item>"""
    rss += "\n</channel>\n</rss>"
    return rss


if __name__ == "__main__":
    articles = fetch_reuters_world()
    rss_feed = generate_rss(articles)
    with open("reuters_world.xml", "w", encoding="utf-8") as f:
        f.write(rss_feed)
