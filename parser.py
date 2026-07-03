# pip install requests bs4 lxml

import requests
from bs4 import BeautifulSoup

def kinoqidir(nom):
    r = requests.post("https://uzbeklar.biz/index.php?do=search", data={
        "do": "search",
        "subaction": "search",
        "search_start": 0,
        "full_search": 0,
        "result_from": 1,
        "story": nom
    })

    natijalar = []

    javob = r.content
    soup = BeautifulSoup(javob, "lxml")

    kinolar = soup.select(".short-item")

    for kino in kinolar:
        nomi = kino.select_one(".short-title").get_text().strip()
        info = kino.select_one(".short-list").get_text().strip()
        havola = kino.select_one(".short-title").get("href")
        natijalar.append({
            "nomi": nomi,
            "info": info,
            "havola": havola
        })

    return natijalar