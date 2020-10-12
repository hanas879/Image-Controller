import json
import os.path
import wget
from bs4 import BeautifulSoup
import requests


def grabIso(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, "lxml")

    news = soup.find("td", class_="NewsText")
    links = news.find_all("a")
    for i in links:
        if ".iso" in i["href"] and "64" in i["href"]:
            print(i["href"])
            break


def checkJSON():
    if os.path.isfile("sources.json") == False:
        with open("sources.json","w") as f:
            f.write("{}")


def saveSources():
    with open("sources.json") as f:
        sources = json.load(f)

    sources["Distro"] = "PLACEHOLDER"

    with open("sources.json", "w") as f:
        json.dump(sources, f, indent=2)


def downloadFile(url):
    wget.download(url)
